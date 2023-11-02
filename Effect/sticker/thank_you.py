import sys
import cv2
import numpy as np
import copy

def thank_you(frame):
    ret = copy.deepcopy(frame)
    thank_you_image = cv2.imread("./Effect/effect_data/sticker/thank_you.png")
    h, w, _ = thank_you_image.shape
    mask = np.where(np.any(thank_you_image > 0, axis=2))
    ret[:h, :w, :][mask[0], mask[1]] = thank_you_image[mask[0], mask[1]]
    return ret

if __name__ == "__main__":
    img_path = sys.argv[1]
    frame = cv2.imread(img_path)
    effected = thank_you(frame)
    while True:
        cv2.imshow("Effect", effected)
        k = cv2.waitKey(1)
        if k == ord("q"):
            break

    cv2.destroyAllWindows()