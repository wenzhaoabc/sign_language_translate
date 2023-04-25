import cv2
import numpy as np

from yolo import YOLO

yolo = YOLO("cross-hands-yolov4-tiny.cfg", "cross-hands-yolov4-tiny.weights", ["hand"])

"""
读取单文件

file = "OIP-C.jpg"

print(file)
mat = cv2.imread(file)

width, height, inference_time, results = yolo.inference(mat)

print("%s in %s seconds: %s classes found!" %
      (os.path.basename(file), round(inference_time, 2), len(results)))

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 848, 640)
print("results = ", results)
for detection in results:
    id, name, confidence, x, y, w, h = detection
    cx = x + (w / 2)
    cy = y + (h / 2)

    # draw a bounding box rectangle and label on the image
    color = (255, 0, 255)
    cv2.rectangle(mat, (x, y), (x + w, y + h), color, 1)
    text = "%s (%s)" % (name, round(confidence, 2))
    cv2.putText(mat, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,
                0.25, color, 1)

    print("%s with %s confidence" % (name, round(confidence, 2)))

    # cv2.imwrite("export.jpg", mat)

# show the output image
cv2.imshow('image', mat)
cv2.waitKey(0)

cv2.destroyAllWindows()
"""


def img_with_hand(pil_image) -> bool:
    """
    检测图片中是否存在手部,返回True或False
    """
    cv_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
    width, height, inference_time, results = yolo.inference(cv_image)
    if len(results) == 0:
        return False
    else:
        return True
