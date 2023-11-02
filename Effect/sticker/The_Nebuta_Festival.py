import sys
import cv2
import numpy as np
import copy
sys.path.append("./Effect")
from effect_base import EffectBase

class The_Nebuta_Festival(EffectBase):
    def __init__(self):
        self.type = "sticker"

    def __call__(self, frame):
        ret = copy.deepcopy(frame)
        The_Nebuta_Festival_image = cv2.imread("./Effect/effect_data/sticker/The_Nebuta_Festival.png")
        height, width, channels = The_Nebuta_Festival_image.shape[:3]
        print("width: " + str(width))
        print("height: " + str(height))
        The_Nebuta_Festival_image = cv2.resize(The_Nebuta_Festival_image, (400, 287))
        h, w, _ = The_Nebuta_Festival_image.shape
        mask = np.where(np.any(The_Nebuta_Festival_image > 0, axis=2))
        ret[:h, :w, :][mask[0], mask[1]] = The_Nebuta_Festival_image[mask[0], mask[1]]
        return True, ret



if __name__ == "__main__":
    img_path = sys.argv[1]
    frame = cv2.imread(img_path)
    effected = The_Nebuta_Festival(frame)
    while True:
        cv2.imshow("Effect", effected)
        k = cv2.waitKey(1)
        if k == ord("q"):
            break

    cv2.destroyAllWindows()