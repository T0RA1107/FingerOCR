import sys
import cv2
import numpy as np
sys.path.append("./Effect")
from effect_base import EffectBase

class Sparkle(EffectBase):
    def __init__(self):
        self.type = "sticker"

    def __call__(self, frame):
        ret = copy.deepcopy(frame)
        sparkle_img = cv2.imread("./Effect/effect_data/sticker/sparkle.png")
        h, w, _ = sparkle_img.shape
        mask = np.where(np.any(sparkle_img > 0, axis=2))
        ret[:h, :w, :][mask[0], mask[1]] = sparkle_img[mask[0], mask[1]]
        return True, ret

if __name__ == "__main__":
    img_path = sys.argv[1]
    frame = cv2.imread(img_path)
    effected = sparkle(frame)
    while True:
        cv2.imshow("Effect", effected)
        k = cv2.waitKey(1)
        if k == ord("q"):
            break

    cv2.destroyAllWindows()