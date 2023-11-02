import sys
import cv2
import numpy as np
import copy
sys.path.append("./Effect")
from effect_base import EffectBase

class Nagoya_Castle(EffectBase):
    def __init__(self):
        self.type = "sticker"

    def __call__(self, frame):
        ret = copy.deepcopy(frame)
        Nagoya_Castle_image = cv2.imread("./Effect/effect_data/sticker/Nagoya_Castle.png")
        height, width, channels = Nagoya_Castle_image.shape[:3]
        print("width: " + str(width))
        print("height: " + str(height))
        Nagoya_Castle_image = cv2.resize(Nagoya_Castle_image, (400, 372))
        h, w, _ = Nagoya_Castle_image.shape
        mask = np.where(np.any(Nagoya_Castle_image > 0, axis=2))
        ret[:h, :w, :][mask[0], mask[1]] = Nagoya_Castle_image[mask[0], mask[1]]
        return True, ret



if __name__ == "__main__":
    img_path = sys.argv[1]
    frame = cv2.imread(img_path)
    effected = Nagoya_Castle(frame)
    while True:
        cv2.imshow("Effect", effected)
        k = cv2.waitKey(1)
        if k == ord("q"):
            break

    cv2.destroyAllWindows()