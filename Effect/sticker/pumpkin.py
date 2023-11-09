import sys
import cv2
import numpy as np
import copy
sys.path.append("./Effect")
from effect_base import EffectBase

class Pumpkin(EffectBase):
    def __init__(self):
        self.type = "sticker"

    def __call__(self, frame):
        ret = copy.deepcopy(frame)
        pumpkin_image = cv2.imread("./Effect/effect_data/sticker/halloween_pumpkin1.png")
        h, w, _ = pumpkin_image.shape
        mask = np.where(np.any(pumpkin_image > 0, axis=2))
        ret[:h, :w, :][mask[0], mask[1]] = pumpkin_image[mask[0], mask[1]]
        ret[2*h:3*h, w:2*w, :][mask[0], mask[1]] = pumpkin_image[mask[0], mask[1]]
        ret[h:2*h, 3*w:4*w, :][mask[0], mask[1]] = pumpkin_image[mask[0], mask[1]]
        return True, ret

def pumpkin(frame):
    ret = copy.deepcopy(frame)
    pumpkin_image = cv2.imread("./Effect/effect_data/sticker/halloween_pumpkin1.png")
    h, w, _ = pumpkin_image.shape
    mask = np.where(np.any(pumpkin_image > 0, axis=2))
    ret[:h, :w, :][mask[0], mask[1]] = pumpkin_image[mask[0], mask[1]]
    ret[2*h:3*h, w:2*w, :][mask[0], mask[1]] = pumpkin_image[mask[0], mask[1]]
    ret[h:2*h, 3*w:4*w, :][mask[0], mask[1]] = pumpkin_image[mask[0], mask[1]]
    return ret

if __name__ == "__main__":
    img_path = sys.argv[1]
    frame = cv2.imread(img_path)
    effected = pumpkin(frame)
    while True:
        cv2.imshow("Effect", effected)
        k = cv2.waitKey(1)
        if k == ord("q"):
            break

    cv2.destroyAllWindows()
