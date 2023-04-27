import time

import cv2
import numpy as np


class YOLO:

    def __init__(self, size=416, confidence=0.5, threshold=0.3):
        self.confidence = confidence
        self.threshold = threshold
        self.size = size
        self.output_names = []
        self.labels = ['hand']
        try:
            self.net = cv2.dnn.readNetFromDarknet(
                'D:\\WorkSpace\\Python\\sign_language\\sign_language_translate\\network\\cross-hands-yolov4-tiny.cfg',
                'D:\\WorkSpace\\Python\\sign_language\\sign_language_translate\\network\\cross-hands-yolov4-tiny.weights')
        except:
            raise ValueError("Couldn't find the models!\nDid you forget to download them manually (and keep in the "
                             "correct directory, models/) or run the shell script?")

        ln = self.net.getLayerNames()
        for i in self.net.getUnconnectedOutLayers():
            self.output_names.append(ln[int(i) - 1])

    def inference_from_file(self, file):
        mat = cv2.imread(file)
        return self.inference(mat)

    def inference(self, image):
        ih, iw = image.shape[:2]

        blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (self.size, self.size), swapRB=True, crop=False)
        self.net.setInput(blob)
        start = time.time()
        layerOutputs = self.net.forward(self.output_names)
        end = time.time()
        inference_time = end - start

        boxes = []
        confidences = []
        classIDs = []

        for output in layerOutputs:
            # loop over each of the detections
            for detection in output:
                # extract the class ID and confidence (i.e., probability) of
                # the current object detection
                scores = detection[5:]
                classID = np.argmax(scores)
                confidence = scores[classID]
                # filter out weak predictions by ensuring the detected
                # probability is greater than the minimum probability
                if confidence > self.confidence:
                    # scale the bounding box coordinates back relative to the
                    # size of the image, keeping in mind that YOLO actually
                    # returns the center (x, y)-coordinates of the bounding
                    # box followed by the boxes' width and height
                    box = detection[0:4] * np.array([iw, ih, iw, ih])
                    (centerX, centerY, width, height) = box.astype("int")
                    # use the center (x, y)-coordinates to derive the top and
                    #  left corner of the bounding box
                    x = int(centerX - (width / 2))
                    y = int(centerY - (height / 2))
                    # update our list of bounding box coordinates, confidences,
                    # and class IDs
                    boxes.append([x, y, int(width), int(height)])
                    confidences.append(float(confidence))
                    classIDs.append(classID)

        idxs = cv2.dnn.NMSBoxes(boxes, confidences, self.confidence, self.threshold)

        results = []
        if len(idxs) > 0:
            for i in idxs.flatten():
                # extract the bounding box coordinates
                x, y = (boxes[i][0], boxes[i][1])
                w, h = (boxes[i][2], boxes[i][3])
                id = classIDs[i]
                confidence = confidences[i]

                results.append((id, self.labels[id], confidence, x, y, w, h))

        return iw, ih, inference_time, results


yolo_model = YOLO()

# yolo_model = YOLO()
#
#
# def img_with_hand(pil_image) -> bool:
#     """
#     检测图片中是否存在手部,返回True或False
#     """
#     cv_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
#     width, height, inference_time, results = yolo_model.inference(cv_image)
#     if len(results) == 0:
#         return False
#     else:
#         return True
#
#
# from PIL import Image
#
# if __name__ == '__main__':
#     img = Image.open("../models/test_imgs/OIP-C.jpeg")
#     res = img_with_hand(img)
#     print(res)
