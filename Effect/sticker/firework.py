import sys
import cv2
import numpy as np
import copy
sys.path.append("./Effect")
from effect_base import EffectBase

class Firework(EffectBase):
    def __init__(self):
        self.type = "sticker"

    def __call__(self, frame):
        ret = copy.deepcopy(frame)
        firework_image = cv2.imread("./Effect/effect_data/sticker/firework.png")
        height, width, channels = firework_image.shape[:3]
        print("width: " + str(width))
        print("height: " + str(height))
        firework_image = cv2.resize(firework_image, (900, 900))
        h, w, _ = firework_image.shape
        mask = np.where(np.any(firework_image > 0, axis=2))
        ret[:h, w:2*w, :][mask[0], mask[1]] = firework_image[mask[0], mask[1]]
        return True, ret

def firework(frame):
    ret = copy.deepcopy(frame)
    firework_image = cv2.imread("./Effect/effect_data/sticker/firework.png")
    height, width, channels = firework_image.shape[:3]
    print("width: " + str(width))
    print("height: " + str(height))
    firework_image = cv2.resize(firework_image, (900, 900))
    h, w, _ = firework_image.shape
    mask = np.where(np.any(firework_image > 0, axis=2))
    ret[:h, w:2*w, :][mask[0], mask[1]] = firework_image[mask[0], mask[1]]
    return ret

if __name__ == "__main__":
    img_path = sys.argv[1]
    frame = cv2.imread(img_path)
    effected = firework(frame)
    while True:
        cv2.imshow("Effect", effected)
        k = cv2.waitKey(1)
        if k == ord("q"):
            break

    cv2.destroyAllWindows()
    