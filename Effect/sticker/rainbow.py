import sys
import cv2
import numpy as np
import copy

def rainbow(frame):
    ret = copy.deepcopy(frame)
    rainbow_image = cv2.imread("./Effect/effect_data/sticker/rainbow.png")
    h, w, _ = rainbow_image.shape
    mask = np.where(np.any(rainbow_image > 0, axis=2))
    ret[:h, :w, :][mask[0], mask[1]] = rainbow_image[mask[0], mask[1]]
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