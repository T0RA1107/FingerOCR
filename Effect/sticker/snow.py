import sys
import cv2
import numpy as np
import copy
sys.path.append("./Effect")
from effect_base import EffectBase

class Snow(EffectBase):
    def __init__(self):
        self.type = "sticker"

    def __call__(self, frame):
        ret = copy.deepcopy(frame)
        snow_img = cv2.imread("./Effect/effect_data/sticker/snow.png")
        snow_img = cv2.resize(snow_img, (100, 100))
        h, w, _ = snow_img.shape
        mask = np.where(np.any(snow_img > 0, axis=2))
        ret[:h, :w, :][mask[0], mask[1]] = snow_img[mask[0], mask[1]]
        ret[:h, 3*w:4*w, :][mask[0], mask[1]] = snow_img[mask[0], mask[1]]
        ret[:h, 8*w:9*w, :][mask[0], mask[1]] = snow_img[mask[0], mask[1]]
        ret[:h, 11*w:12*w, :][mask[0], mask[1]] = snow_img[mask[0], mask[1]]
        # ret[:h, 15*w:16*w, :][mask[0], mask[1]] = snow_img[mask[0], mask[1]]
        ret[h:2*h, 2*w:3*w, :][mask[0], mask[1]] = snow_img[mask[0], mask[1]]
        ret[h:2*h, 4*w:5*w, :][mask[0], mask[1]] = snow_img[mask[0], mask[1]]
        ret[h:2*h, 5*w:6*w, :][mask[0], mask[1]] = snow_img[mask[0], mask[1]]
        ret[h:2*h, 10*w:11*w, :][mask[0], mask[1]] = snow_img[mask[0], mask[1]]
        # ret[h:2*h, 17*w:18*w, :][mask[0], mask[1]] = snow_img[mask[0], mask[1]]
        ret[2*h:3*h, 1*w:2*w, :][mask[0], mask[1]] = snow_img[mask[0], mask[1]]
        ret[2*h:3*h, 8*w:9*w, :][mask[0], mask[1]] = snow_img[mask[0], mask[1]]
        # ret[2*h:3*h, 13*w:14*w, :][mask[0], mask[1]] = snow_img[mask[0], mask[1]]
        # ret[2*h:3*h, 16*w:17*w, :][mask[0], mask[1]] = snow_img[mask[0], mask[1]]
        h, w, _ = snow_img.shape
        mask = np.where(np.any(snow_img > 0, axis=2))
        ret[:h, :w, :][mask[0], mask[1]] = snow_img[mask[0], mask[1]]
        return True, ret

def snow(frame):
    ret = copy.deepcopy(frame)
    snow_img = cv2.imread("./Effect/effect_data/sticker/snow.png")
    height, width, channels = snow_img.shape[:3]
    print("width: " + str(width))
    print("height: " + str(height))
    snow_img = cv2.resize(snow_img, (100, 100))
    h, w, _ = snow_img.shape
    mask = np.where(np.any(snow_img > 0, axis=2))
    ret[:h, :w, :][mask[0], mask[1]] = snow_img[mask[0], mask[1]]
    ret[:h, 3*w:4*w, :][mask[0], mask[1]] = snow_img[mask[0], mask[1]]
    ret[:h, 8*w:9*w, :][mask[0], mask[1]] = snow_img[mask[0], mask[1]]
    ret[:h, 11*w:12*w, :][mask[0], mask[1]] = snow_img[mask[0], mask[1]]
    ret[:h, 15*w:16*w, :][mask[0], mask[1]] = snow_img[mask[0], mask[1]]
    ret[h:2*h, 2*w:3*w, :][mask[0], mask[1]] = snow_img[mask[0], mask[1]]
    ret[h:2*h, 4*w:5*w, :][mask[0], mask[1]] = snow_img[mask[0], mask[1]]
    ret[h:2*h, 5*w:6*w, :][mask[0], mask[1]] = snow_img[mask[0], mask[1]]
    ret[h:2*h, 10*w:11*w, :][mask[0], mask[1]] = snow_img[mask[0], mask[1]]
    ret[h:2*h, 17*w:18*w, :][mask[0], mask[1]] = snow_img[mask[0], mask[1]]
    ret[2*h:3*h, 1*w:2*w, :][mask[0], mask[1]] = snow_img[mask[0], mask[1]]
    ret[2*h:3*h, 8*w:9*w, :][mask[0], mask[1]] = snow_img[mask[0], mask[1]]
    ret[2*h:3*h, 13*w:14*w, :][mask[0], mask[1]] = snow_img[mask[0], mask[1]]
    ret[2*h:3*h, 16*w:17*w, :][mask[0], mask[1]] = snow_img[mask[0], mask[1]]
    return ret

if __name__ == "__main__":
    img_path = sys.argv[1]
    frame = cv2.imread(img_path)
    effected = snow(frame)
    while True:
        cv2.imshow("Effect", effected)
        k = cv2.waitKey(1)
        if k == ord("q"):
            break

    cv2.destroyAllWindows()
    