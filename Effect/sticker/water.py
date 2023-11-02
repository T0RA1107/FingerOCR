import sys
import cv2
import numpy as np
import copy

def drop(frame):
    drop_img = cv2.imread("./Effect/effect_data/sticker/drop.png")
    h, w, _ = drop_img.shape
    print(drop_img[0][0])
    ret = copy.deepcopy(frame)
    mask = np.where(np.any(drop_img > 0, axis=2))
    ret[:h, :w, :][mask[0], mask[1]] = drop_img[mask[0], mask[1]]
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

