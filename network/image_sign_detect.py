import os

import cv2
import numpy as np
import torch

from .Model.network import Net

signs = {'0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '7': 'H', '8': 'I',
         '10': 'K', '11': 'L', '12': 'M', '13': 'N', '14': 'O', '15': 'P', '16': 'Q', '17': 'R',
         '18': 'S', '19': 'T', '20': 'U', '21': 'V', '22': 'W', '23': 'X', '24': 'Y'}


class Static_Sign_Language_Recognition():
    def __init__(self):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = Net()
        self.model.to(self.device)

        # if torch.cuda.is_available():
        project_path = os.path.abspath('.')
        static_path = os.path.join(project_path, 'static')
        checkpoint_path = os.path.join(static_path, 'image_sign_detect_weight.pt')
        # checkpoint = r"weights/model.pt"
        checkpoints = torch.load(checkpoint_path)
        self.model.load_state_dict(checkpoints)

        self.model.eval()

    def preProcess(self, img):
        res = cv2.resize(img, dsize=(28, 28), interpolation=cv2.INTER_CUBIC)
        res = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
        res1 = np.reshape(res, (1, 1, 28, 28)) / 255
        res2 = torch.from_numpy(res1)
        res3 = res2.type(torch.FloatTensor).to(self.device)
        return res3

    # 外部接口
    def predict(self, path):
        with torch.no_grad():
            image = cv2.imread(path)
            new_image = self.preProcess(image)
            out = self.model(new_image)
            probs, label = torch.topk(out, 25)
            probs = torch.nn.functional.softmax(probs, 1)
            pred = out.max(1, keepdim=True)[1]

            if float(probs[0, 0]) < 0.2:
                print('Sign not detected')
                return None, None
            else:
                text = signs[str(int(pred))]
                accuracy = '{:.2f}'.format(float(probs[0, 0])) + '%'

                print("Prediction = ", text)
                print("Accuracy = ", accuracy)
                return text, accuracy

# if __name__ == "__main__":
#     # Initialize the Static_Sign_Language_Recognition class
#     sslr = Static_Sign_Language_Recognition()
#
#     # Test on an image
#     path = r"./test_images/P.png"
#     translation, accuracy = sslr.predict(path)
#     print("Translation: ", translation)
#     print("Accuracy: ", accuracy)
