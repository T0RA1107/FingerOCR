import sys
import cv2
import numpy as np
import copy
sys.path.append("./Effect")
from effect_base import EffectBase

class Drop(EffectBase):
    def __init__(self):
        self.type = "sticker"

    def __call__(self, frame):
        ret = copy.deepcopy(frame)
        drop_image = cv2.imread("./Effect/effect_data/sticker/drop.png")
        h, w, _ = drop_image.shape
        mask = np.where(np.any(drop_image > 0, axis=2))
        ret[:h, :w, :][mask[0], mask[1]] = drop_image[mask[0], mask[1]]
        return True, ret

def drop(frame):
    ret = copy.deepcopy(frame)
    drop_image = cv2.imread("./Effect/effect_data/sticker/drop.png")
    h, w, _ = drop_image.shape
    mask = np.where(np.any(drop_image > 0, axis=2))
    ret[:h, :w, :][mask[0], mask[1]] = drop_image[mask[0], mask[1]]
    return ret

if __name__ == "__main__":
    img_path = sys.argv[1]
    frame = cv2.imread(img_path)
    effected = drop(frame)
    while True:
        cv2.imshow("Effect", effected)
        k = cv2.waitKey(1)
        if k == ord("q"):
            break

    cv2.destroyAllWindows()
