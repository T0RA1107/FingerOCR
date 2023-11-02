import sys
import cv2
import numpy as np
import copy
sys.path.append("./Effect")
from effect_base import EffectBase

class Tokyo_Metropolitan_Government(EffectBase):
    def __init__(self):
        self.type = "sticker"

    def __call__(self, frame):
        ret = copy.deepcopy(frame)
        Tokyo_Metropolitan_Government_image = cv2.imread("./Effect/effect_data/sticker/Tokyo_Metropolitan_Government.png")
        height, width, channels = Tokyo_Metropolitan_Government_image.shape[:3]
        print("width: " + str(width))
        print("height: " + str(height))
        Tokyo_Metropolitan_Government_image = cv2.resize(Tokyo_Metropolitan_Government_image, (280, 400))
        h, w, _ = Tokyo_Metropolitan_Government_image.shape
        mask = np.where(np.any(Tokyo_Metropolitan_Government_image > 0, axis=2))
        ret[:h, :w, :][mask[0], mask[1]] = Tokyo_Metropolitan_Government_image[mask[0], mask[1]]
        return True, ret

def tokyo_metropolitan_government(frame):
    ret = copy.deepcopy(frame)
    Tokyo_Metropolitan_Government_image = cv2.imread("./Effect/effect_data/sticker/Tokyo_Metropolitan_Government.png")
    height, width, channels = Tokyo_Metropolitan_Government_image.shape[:3]
    print("width: " + str(width))
    print("height: " + str(height))
    Tokyo_Metropolitan_Government_image = cv2.resize(Tokyo_Metropolitan_Government_image, (280, 400))
    h, w, _ = Tokyo_Metropolitan_Government_image.shape
    mask = np.where(np.any(Tokyo_Metropolitan_Government_image > 0, axis=2))
    ret[:h, :w, :][mask[0], mask[1]] = Tokyo_Metropolitan_Government_image[mask[0], mask[1]]

if __name__ == "__main__":
    img_path = sys.argv[1]
    frame = cv2.imread(img_path)
    effected = tokyo_metropolitan_government(frame)
    while True:
        cv2.imshow("Effect", effected)
        k = cv2.waitKey(1)
        if k == ord("q"):
            break

    cv2.destroyAllWindows()