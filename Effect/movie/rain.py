import sys
import cv2
import numpy as np
import copy
sys.path.append("./Effect")
from effect_base import EffectBase

class Rain(EffectBase):
    def __init__(self):
        self.type = "movie"
        self.capture = cv2.VideoCapture("./Effect/effect_data/movie/rain_01.mp4")
        self.SE = "./Sound/rain/雨・傘の下（激しい）.mp3"

    def __call__(self, frame):
        ret, image = self.capture.read()
        if not ret:
            return False, frame
        ret = copy.deepcopy(frame)
        H, W, _ = frame.shape
        h, w, _ = image.shape
        if H < h or W < w:
            image = cv2.resize(image, dsize=(W, H))
        mask = np.where(np.any(image > 50, axis=2))
        ret[:h, :w, :][mask[0], mask[1]] = image[mask[0], mask[1]]
        return True, ret

def rain_capture():
    return cv2.VideoCapture("./Effect/effect_data/movie/rain_01.mp4")

def thunder_SE():
    return "./Sound/rain/雨・傘の下（激しい）.mp3"

if __name__ == "__main__":
    img_path = sys.argv[1]
    frame = cv2.imread(img_path)
    cap = cv2.VideoCapture("./Effect/effect_data/movie/rain_01.mp4")
    while True:
        is_ok, rain_image = cap.read()
        if not is_ok:
            break
        ret = copy.deepcopy(frame)
        h, w, _ = rain_image.shape
        mask = np.where(np.any(rain_image > 50, axis=2))
        ret[:h, :w, :][mask[0], mask[1]] = rain_image[mask[0], mask[1]]
        cv2.imshow("Effect", ret)
        k = cv2.waitKey(1)
        if k == ord("q"):
            break

    cv2.destroyAllWindows()
