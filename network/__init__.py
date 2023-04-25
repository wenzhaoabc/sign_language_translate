# -*- coding: utf-8 -*-
import os
import logging
import cv2
from PIL import Image
import numpy as np
from datetime import datetime
import torch
from sklearn.metrics import accuracy_score
from models.Seq2Seq import Encoder, Decoder, Seq2Seq
# from dataset_modify import CSL_Continuous, CSL_Continuous_Char
import torch.nn as nn
# from torch.utils.data import DataLoader
# from torch.utils.tensorboard import SummaryWriter
import torchvision.transforms as transforms
# import argparse

# learning_rate = 1e-4
# weight_decay = 1e-5
sample_size = 128
# sample_duration = 48
enc_hid_dim = 512
emb_dim = 256
dec_hid_dim = 512
dropout = 0.5
# clip = 1
# log_interval = 100

#参考，对应修改
def preprocess(image_path):
    input_size = 224
    mean = [0.485, 0.456, 0.406]
    std = [0.229, 0.224, 0.225]

    transform = transforms.Compose([
        transforms.Resize(input_size),
        transforms.CenterCrop(input_size),
        transforms.ToTensor(),
        transforms.Normalize(mean, std)
    ])

    image = Image.open(image_path).convert('RGB')
    tensor = transform(image)
    return tensor.unsqueeze(0)



#Step 3:模型后处理（返回模型预测的结果——转为用户需要的方式）
def postprocess(output, labels):
    _, predicted = torch.max(output, 1)
    return labels[predicted.item()]



# 将上述内容封装成类
class ModelWrapper:
    def __init__(self, model_path, labels_path,frames=64,transform=None):
        self.model_path = model_path #'./MyModel/seq2seq_models/slr_seq2seq_epoch001.pth'
        self.labels_path = labels_path #'./dictionary.txt'
        self.frames = frames#帧数，在读取视频时遇到
        self.transform = transforms.Compose([transforms.Resize([128, 128]), transforms.ToTensor()])#是否对图像转置
        self.read_dict()
        self.images=[]

        os.environ['NUMEXPR_MAX_THREADS'] ='12'
        os.environ["CUDA_VISIBLE_DEVICES"]="0"

        print(torch.cuda.is_available())
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(self.device)

        # Run the model parallelly
        encoder = Encoder(lstm_hidden_size=enc_hid_dim, arch="resnet34").to(self.device)
        decoder = Decoder(output_dim=self.output_dim, emb_dim=emb_dim, enc_hid_dim=enc_hid_dim, dec_hid_dim=dec_hid_dim, dropout=dropout).to(self.device)
        self.model = Seq2Seq(encoder=encoder, decoder=decoder, device=self.device).to(self.device)
        if torch.cuda.device_count() > 1:
            # logger.info("Using {} GPUs".format(torch.cuda.device_count()))
            self.model = nn.DataParallel(self.model)
        # Create loss criterion & optimizer
        criterion = nn.CrossEntropyLoss()
        # Load model
        self.model.load_state_dict(torch.load(model_path,map_location='cuda:0'))
        self.model.eval()

    def read_images(self, folder_path):
        # 在条件不满足程序运行的情况下直接返回错误，而不必等待程序运行后出现崩溃
        # assert len(os.listdir(folder_path)) >= self.frames, "Too few images in your data folder: " + str(folder_path)

        images = []  # list
        capture = cv2.VideoCapture(folder_path)

        # fps = capture.get(cv2.CAP_PROP_FPS)
        fps_all = capture.get(cv2.CAP_PROP_FRAME_COUNT)
        # 取整数部分
        timeF = int(fps_all / self.frames)
        n = 1

        # 对一个视频文件进行操作
        while capture.isOpened():
            ret, frame = capture.read()
            if ret is False:
                break
            # 每隔timeF帧进行存储操作
            if (n % timeF == 0):
                image = frame  # frame是PIL
                image = Image.fromarray(image)  # np array
                if self.transform is not None:
                    image = self.transform(image)  # tensor
                images.append(image)
            n = n + 1
            # cv2.waitKey(1)
        capture.release()
        # print('读取视频完成')
        # print("采样间隔：", timeF)

        lenB = len(images)
        # 将列表随机去除一部分元素，剩下的顺序不变

        for o in range(0, int(lenB - self.frames)):
            # 删除一个长度内随机索引对应的元素，不包括len(images)即不会超出索引
            del images[np.random.randint(0, len(images))]
            # images.pop(np.random.randint(0, len(images)))
        lenF = len(images)
        # 沿着一个新维度对输入张量序列进行连接，序列中所有的张量都应该为相同形状
        images = torch.stack(images, dim=0)
        # 原本是帧，通道，h，w，需要换成可供3D CNN使用的形状
        images = images.permute(1, 0, 2, 3)

        # print("数据类型：", images.dtype)
        # print("图像形状：", images.shape)
        # print("总帧数：%d, 采样后帧数：%d, 抽帧后帧数：%d" % (fps_all, lenB, lenF))
        # print(images)
        return images
    
    # 单帧读取
    def _read_images(self, image):
        image = Image.fromarray(image)  # np array
        if self.transform is not None:
            image = self.transform(image)  # tensor
        self.images.append(image)
        # lenB = len(self.images)

        # for o in range(0, int(lenB - self.frames)):
            # del images[np.random.randint(0, len(images))]
        # lenF = len(images)
        self.images = torch.stack(self.images, dim=0)

        # return self.images

    def get_key(self,val):
        for key, value in self.dict.items():
            if val == value:
                return key
    
    def read_dict(self):
    # dictionary
        self.dict = {'<pad>': 0, '<sos>': 1, '<eos>': 2}
        self.output_dim = 3
        try:
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
    
    # def predict(self, image_path):
    def predict(self, image_):
        # get the inputs and labels
        # images = self.read_images(image_path)
        self._read_images(image_)

        images=self.images.permute(1, 0, 2, 3)
        print(images.shape)
        inputs = (images.unsqueeze(0)).to(self.device)
        mmm=torch.LongTensor([1,247,506,215,110,294,2,1,247,506,215,110,294,2,0,0,0,0])
        labels = mmm.unsqueeze(0).to(self.device)
        # labels = torch.ones(9).unsqueeze(0).to(self.device)
        # forward
        # print(inputs.shape)
        # print(type(inputs))
        # print(type(inputs[0]))
        # print(type(inputs[0][0][0]))
        # print(labels.shape)
        # print(type(labels))
        # print(type(labels[0]))
        outputs = self.model(inputs,labels,0)
        # print(outputs.shape)
        output_dim = outputs.shape[-1]
        outputs = outputs[1:].view(-1, output_dim)
        # print(outputs.shape)
        # print(outputs)
        prediction = torch.max(outputs, 1)[1]
        # print(prediction)
        prediction = prediction.view(-1, 1).permute(1,0).tolist()#prediction.view(-1, batch_size).permute(1,0).tolist()
        # print(prediction)
        for i in range(0,len(prediction)):
            res=''
            for p2 in prediction[i]:
                key=self.get_key(p2)
                res=res+key
            print("prediction:",res)

        # input_tensor = preprocess(image_path)#需要修改成我们的
        # with torch.no_grad():
        #     output = self.model(input_tensor)#需要修改成我们的
        # return postprocess(output, self.labels)#需要修改成我们的
    

# m=ModelWrapper("./model/slr_seq2seq_epoch001.pth","./dictionary/dictionary.txt")
# m.predict("./img/P01_s1_00_0_color.avi")

m=ModelWrapper("/content/drive/MyDrive/Cur_Continuous_SLR/SLR/MyModel/seq2seq_models/slr_seq2seq_epoch083.pth","./dictionary.txt")
# m.predict("/content/drive/MyDrive/Cur_Continuous_SLR/SLR/1-（手语）你一定要开心-480P 清晰-HEVC.mp4")
# m.predict("/content/drive/MyDrive/Cur_Continuous_SLR/SLR/mydataset/Continuous_SLR_dataset/color/000039/P08_s4_09_4_color.avi")
# m.predict("/content/drive/MyDrive/Cur_Continuous_SLR/SLR/P10_s4_09_4_color.mp4")
# m.predict("/content/drive/MyDrive/Cur_Continuous_SLR/SLR/1-手语日常交流---“你好吗？”-480P 清晰-AVC.mp4")
# m.predict("/content/drive/MyDrive/Cur_Continuous_SLR/SLR/mydataset/Continuous_SLR_dataset/color/000010/P01_s2_00_0_color.avi")

