import sys
import cv2
import numpy as np
import copy
sys.path.append("./Effect")
from effect_base import EffectBase

class Star(EffectBase):
    def __init__(self):
        self.type = "movie"
        self.capture = cv2.VideoCapture("./Effect/effect_data/movie/star_03.mp4")
        self.SE = "./Sound/Thunder/天候・雷08.mp3"

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

def star_capture():
    return cv2.VideoCapture("./Effect/effect_data/movie/star_03.mp4")

def star_SE():
    return "./Sound/Thunder/天候・雷08.mp3"

def star_capture():
    return cv2.VideoCapture("./Effect/effect_data/movie/star_03.mp4")

def star(frame, star_image):
    ret = copy.deepcopy(frame)
    H, W, _ = frame.shape
    h, w, _ = star_image.shape
    if H < h or W < w:
        rate = min(h / H, w / W)
        star_image = cv2.resize(star_image, fx=rate, fy=rate)
    mask = np.where(np.any(star_image > 50, axis=2))
    ret[:h, :w, :][mask[0], mask[1]] = star_image[mask[0], mask[1]]
    return ret

if __name__ == "__main__":
    img_path = sys.argv[1]
    frame = cv2.imread(img_path)
    cap = cv2.VideoCapture("./Effect/effect_data/movie/star_03.mp4")
    while True:
        is_ok, star_image = cap.read()
        if not is_ok:
            break
        ret = copy.deepcopy(frame)
        h, w, _ = star_image.shape
        mask = np.where(np.any(star_image > 50, axis=2))
        ret[:h, :w, :][mask[0], mask[1]] = star_image[mask[0], mask[1]]
        cv2.imshow("Effect", ret)
        k = cv2.waitKey(1)
        if k == ord("q"):
            break

    cv2.destroyAllWindows()
