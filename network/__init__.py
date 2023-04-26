import os
import threading
from queue import Queue

import cv2
import numpy as np
import torch

import torch.nn as nn

import torchvision.transforms as transforms
from PIL import Image

from api.routes import send_translated_texy
from models.Seq2Seq import Encoder, Decoder, Seq2Seq
from network.hand_detect import YOLO

yolo_model = YOLO()

# Global Virables
sample_size = 128
# sample_duration = 48
enc_hid_dim = 512
emb_dim = 256
dec_hid_dim = 512
dropout = 0.5


def img_with_hand(pil_image) -> bool:
    """
    检测图片中是否存在手部,返回True或False
    """
    cv_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    width, height, inference_time, results = yolo_model.inference(cv_image)
    if len(results) == 0:
        return False
    else:
        return True


# ModelWrapper类
# ModelWrapper负责实现接受前端数据，输出翻译结果的全过程
# 包括缓冲区1，yolo识别模型，缓冲区2，翻译模型
class ModelWrapper:
    def __init__(self, model_path="models/params/slr_seq2seq_epoch107.pth", labels_path="models/params/dictionary.txt",
                 frames=64, transform=None):
        # -------------------------------------------------#
        # SLR model
        self.model_path = model_path  # './MyModel/seq2seq_models/slr_seq2seq_epoch001.pth'
        self.labels_path = labels_path  # './dictionary.txt'
        self.frames = frames  # 帧数，在读取视频时遇到
        self.transform = transforms.Compose([transforms.Resize([128, 128]), transforms.ToTensor()])  # 是否对图像变换
        self.read_dict()
        self.images = []

        os.environ['NUMEXPR_MAX_THREADS'] = '12'
        os.environ["CUDA_VISIBLE_DEVICES"] = "0"

        print(torch.cuda.is_available())
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(self.device)

        # Run the model parallelly
        encoder = Encoder(lstm_hidden_size=enc_hid_dim, arch="resnet34").to(self.device)
        # encoder = Encoder(lstm_hidden_size=enc_hid_dim).to(self.device)
        decoder = Decoder(output_dim=self.output_dim, emb_dim=emb_dim, enc_hid_dim=enc_hid_dim, dec_hid_dim=dec_hid_dim,
                          dropout=dropout).to(self.device)
        self.model = Seq2Seq(encoder=encoder, decoder=decoder, device=self.device).to(self.device)
        if torch.cuda.device_count() > 1:
            # logger.info("Using {} GPUs".format(torch.cuda.device_count()))
            self.model = nn.DataParallel(self.model)
        # Create loss criterion & optimizer
        criterion = nn.CrossEntropyLoss()
        # Load model
        self.model.load_state_dict(torch.load(model_path, map_location='cuda:0'))
        self.model.eval()

        self.continuous_not_hand_num = 0  # 连续没有手的数量
        self.MAX_NOT_HAND_NUM = 5  # 连续没有手的图像数——判断何时结束

        # -------------------------------------------------#
        # image buffer
        self.image_buffer1 = Queue()  # 介于前端传来的数据——yolo模型间
        self.image_buffer2 = Queue()  # 介于yolo模型输出———手语翻译模型间
        # self.hand_flag = True  # 判断是否接受当前图像（是否识别到手）

        self.lock = threading.Lock()  # 线程锁
        self.queue2_lock = False  # false代表可以往queue2中写数据，true代表不可以，只能读数据

    # SLR model
    def get_key(self, val):
        for key, value in self.dict.items():
            if val == value:
                return key

    def read_dict(self):
        # dictionary
        self.dict = {'<pad>': 0, '<sos>': 1, '<eos>': 2}
        self.output_dim = 3
        try:
            print(self.labels_path)

            dict_file = open(self.labels_path, 'r', encoding='utf-8')
            for line in dict_file.readlines():
                line = line.strip().split('\t')
                # word with multiple expressions
                if '（' in line[1] and '）' in line[1]:
                    for delimeter in ['（', '）', '、']:
                        line[1] = line[1].replace(delimeter, " ")
                    words = line[1].split()
                else:
                    words = [line[1]]
                for word in words:
                    self.dict[word] = self.output_dim
                self.output_dim += 1
        except Exception as e:
            raise

    def predict(self):
        # get the inputs and labels
        if self.image_buffer2.empty():
            print("No entered!")
            return None

        print("Entered")
        images = []
        while not self.image_buffer2.empty():
            image = self.image_buffer2.get()  # 从队列中取出元素并弹出
            # print(type(image))
            # print(image.shape)
            # image = np.asarray(image)  # np array
            if self.transform is not None:
                image = self.transform(image)  # tensor
            images.append(image)

        # 沿着一个新维度对输入张量序列进行连接，序列中所有的张量都应该为相同形状
        images = torch.stack(images, dim=0)
        # 原本是帧，通道，h，w，需要换成可供3D CNN使用的形状
        images = images.permute(1, 0, 2, 3)

        print(images.shape)

        inputs = (images.unsqueeze(0)).to(self.device)
        mmm = torch.LongTensor([1, 247, 506, 215, 110, 294, 2, 1, 247, 506, 215, 110, 294, 2, 0, 0, 0, 0])
        labels = mmm.unsqueeze(0).to(self.device)
        outputs = self.model(inputs, labels, 0)
        # print(outputs.shape)
        output_dim = outputs.shape[-1]
        outputs = outputs[1:].view(-1, output_dim)
        # print(outputs.shape)
        # print(outputs)
        prediction = torch.max(outputs, 1)[1]
        # print(prediction)
        prediction = prediction.view(-1, 1).permute(1,
                                                    0).tolist()  # prediction.view(-1, batch_size).permute(1,0).tolist()
        for i in range(0, len(prediction)):
            res = ''
            for p2 in prediction[i]:
                key = self.get_key(p2)
                if key == '<eos>':
                    break
                res = res + key

            print("prediction:", res)
        return res  # 手语翻译结果

    # image buffer——get image from 前端
    def add_image_toQueue1(self, image):  # 从前端无条件读取数据并保留
        # self.lock.acquire()

        if isinstance(image, Image.Image):
            self.image_buffer1.put(image)
            # print("Image added to queue 1 !")
            print("Len:", self.image_buffer1.qsize())
        else:
            print("Error: For queue 1 Input is not an image object.")

        # self.lock.release()

    def add_image_toQueue2(self):  # 从yolo模型读取flag,flag决定是否将buffer1的数据读到buffer2, 都要弹出buffer1
        if self.queue2_lock:
            return False
        if self.image_buffer1.qsize() < 2:  # 当前img个数大等于2才读，防止同时读写一个img
            # print("WARNING: Queue1 Image is not enough !")
            return False
        # self.lock.acquire()

        image = self.image_buffer1.get()  # 从队列中取出元素并弹出

        # self.lock.release()

        hand_flag = img_with_hand(image)
        if hand_flag:
            self.continuous_not_hand_num = 0
            self.image_buffer2.put(image)
        else:
            if self.continuous_not_hand_num >= self.MAX_NOT_HAND_NUM:  # 取出queue2的所有元素返回，用于判断
                return True  # 返回True表示可以取走Queue2的所有元素
            else:
                self.continuous_not_hand_num += 1
                self.image_buffer2.put(image)

        return False

    def get_and_predict(self):
        while True:
            # sleep(50)
            flag = self.add_image_toQueue2()
            # print(self.continuous_not_hand_num)
            if flag and not self.queue2_lock:  # 可以进行预测的标志
                print("enough")
                print(self.image_buffer2.qsize())
                # print(self.image_buffer2.empty())
                res = self.predict()
                print(res)
                send_translated_texy(res)
                # ?? // 关闭线程

                # return res
                # print(res)
            # else:
            # print("No enough")
            # return None


if __name__ == '__main__':
    mymodel = ModelWrapper("models/params/slr_seq2seq_epoch107.pth",
                           "models/params/dictionary.txt")

    img1 = Image.open("models/test_imgs/OIP-C.jpeg")
    img2 = Image.open("models/test_imgs/test2.jpeg")
    res = img_with_hand(img1)
    print(res)
    res = img_with_hand(img2)
    print(res)
    # 开启 2 个线程，分别执行 func1 和 func2 函数

    t2 = threading.Thread(target=mymodel.get_and_predict)
    t2.start()
    num = 0
    while True:
        if num < 20:
            t1 = threading.Thread(target=mymodel.add_image_toQueue1, args=(img1,))
            t1.start()
        elif num < 30:
            t1 = threading.Thread(target=mymodel.add_image_toQueue1, args=(img2,))
            t1.start()
        elif num < 40:
            t1 = threading.Thread(target=mymodel.add_image_toQueue1, args=(img1,))
            t1.start()
        else:
            t1 = threading.Thread(target=mymodel.add_image_toQueue1, args=(img2,))
            t1.start()
        num += 1
        if num >= 50:
            break
    # t2.join()

"""
一个函数
异步函数

无手NUM = 0
def add_img(img:PIL.Image):
    异步 async  (img -> yolo:)
    await result
     result ->:
        true -> 加入list 无手NUM=0
        false -> 无手NUM += 1 ； 无手NUM > 某个值 -》 list -> MODEL -> res (call send_translated_texy(res))
"""
