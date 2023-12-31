import sys
import cv2
import numpy as np
import copy
sys.path.append("./Effect")
from effect_base import EffectBase

class Rainbow(EffectBase):
    def __init__(self):
        self.type = "sticker"

    def __call__(self, frame):
        ret = copy.deepcopy(frame)    
        rainbow_image = cv2.imread("./Effect/effect_data/sticker/rainbow.png")
        rainbow_image = rainbow_image[100:400, :]
        h, w, _ = rainbow_image.shape
        mask = np.where(np.any(rainbow_image > 0, axis=2))
        ret[:h, :w, :][mask[0], mask[1]] = rainbow_image[mask[0], mask[1]]
        return True, ret

def rainbow(frame):
    ret = copy.deepcopy(frame)
    rainbow_image = cv2.imread("./Effect/effect_data/sticker/rainbow.png")
    rainbow_image = cv2.resize(rainbow_image, (700, 700))
    h, w, _ = rainbow_image.shape
    mask = np.where(np.any(rainbow_image > 0, axis=2))
    ret[:h, 250:, :][mask[0], mask[1]] = rainbow_image[mask[0], mask[1]]
    return ret
    
if __name__ == "__main__":
    img_path = sys.argv[1]
    frame = cv2.imread(img_path)
    effected = rainbow(frame)
    while True:
        cv2.imshow("Effect", effected)
        k = cv2.waitKey(1)
        if k == ord("q"):
            break

    cv2.destroyAllWindows()
