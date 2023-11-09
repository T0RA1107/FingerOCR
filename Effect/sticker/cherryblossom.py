import sys
import cv2
import numpy as np
import copy
sys.path.append("./Effect")
from effect_base import EffectBase

class Cherryblossom(EffectBase):
    def __init__(self):
        self.type = "sticker"

    def __call__(self, frame):
        ret = copy.deepcopy(frame)
        cherryblossom_image = cv2.imread("./Effect/effect_data/sticker/cherryblossom.png")
        sakurahubuki_image = cv2.imread("./Effect/effect_data/sticker/sakura_fubuki.png")
        h, w, _ = cherryblossom_image.shape
        h1, w1, _ = sakurahubuki_image.shape
        mask = np.where(np.any(cherryblossom_image > 0, axis=2))
        mask1 = np.where(np.any(sakurahubuki_image > 0, axis=2))
        ret[:h, -w:, :][mask[0], mask[1]] = cherryblossom_image[mask[0], mask[1]]
        ret[-h1:, :w1, :][mask1[0], mask1[1]] = sakurahubuki_image[mask1[0], mask1[1]]
        return True, ret

def cherryblossom(frame):
    ret = copy.deepcopy(frame)
    cherryblossom_image = cv2.imread("./Effect/effect_data/sticker/cherryblossom.png")
    sakurahubuki_image = cv2.imread("./Effect/effect_data/sticker/sakura_fubuki.png")
    h, w, _ = cherryblossom_image.shape
    h1, w1, _ = sakurahubuki_image.shape
    mask = np.where(np.any(cherryblossom_image > 0, axis=2))
    mask1 = np.where(np.any(sakurahubuki_image > 0, axis=2))
    ret[:h, -w:, :][mask[0], mask[1]] = cherryblossom_image[mask[0], mask[1]]
    ret[-h1:, :w1, :][mask1[0], mask1[1]] = sakurahubuki_image[mask1[0], mask1[1]]
    return ret

if __name__ == "__main__":
    img_path = sys.argv[1]
    frame = cv2.imread(img_path)
    effected = cherryblossom(frame)
    while True:
        cv2.imshow("Effect", effected)
        k = cv2.waitKey(1)
        if k == ord("q"):
            break

    cv2.destroyAllWindows()