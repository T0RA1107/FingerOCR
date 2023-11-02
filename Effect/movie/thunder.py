import sys
import cv2
import numpy as np
import copy
from effect_base import EffectBase

class Thunder(EffectBase):
    def __init__(self):
        self.type = "movie"
        self.capture = cv2.VideoCapture("./Effect/effect_data/thunder_04.mp4")
        self.SE = "./Sound/Thunder/天候・雷08.mp3"

    def __call__(self, frame):
        ret, image = self.capture.read()
        if not ret:
            return False, frame
        ret = copy.deepcopy(frame)
        H, W, _ = frame.shape
        h, w, _ = image.shape
        if H < h or W < w:
            rate = min(h / H, w / W)
            image = cv2.resize(image, fx=rate, fy=rate)
        mask = np.where(np.any(image > 50, axis=2))
        ret[:h, :w, :][mask[0], mask[1]] = image[mask[0], mask[1]]
        return True, ret

def thunder_capture():
    return cv2.VideoCapture("./Effect/effect_data/thunder_04.mp4")

def thunder_SE():
    return "./Sound/Thunder/天候・雷08.mp3"

def thunder(frame, thunder_image):
    ret = copy.deepcopy(frame)
    H, W, _ = frame.shape
    h, w, _ = thunder_image.shape
    if H < h or W < w:
        rate = min(h / H, w / W)
        thunder_image = cv2.resize(thunder_image, fx=rate, fy=rate)
    mask = np.where(np.any(thunder_image > 50, axis=2))
    ret[:h, :w, :][mask[0], mask[1]] = thunder_image[mask[0], mask[1]]
    return ret

if __name__ == "__main__":
    img_path = sys.argv[1]
    frame = cv2.imread(img_path)
    cap = cv2.VideoCapture("./Effect/effect_data/thunder_04.mp4")
    while True:
        is_ok, thunder_image = cap.read()
        if not is_ok:
            break
        ret = copy.deepcopy(frame)
        h, w, _ = thunder_image.shape
        mask = np.where(np.any(thunder_image > 50, axis=2))
        ret[:h, :w, :][mask[0], mask[1]] = thunder_image[mask[0], mask[1]]
        cv2.imshow("Effect", ret)
        k = cv2.waitKey(1)
        if k == ord("q"):
            break

    cv2.destroyAllWindows()
