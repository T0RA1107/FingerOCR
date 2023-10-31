import sys
import cv2
import numpy as np

def sparkle(frame):
    sparkle_img = cv2.imread("./Effect/effect_data/sparkle.png")
    h, w, _ = sparkle_img.shape
    ret = copy.deepcopy(frame)
    mask = np.where(np.any(sparkle_img > 0, axis=2))
    ret[:h, :w, :][mask[0], mask[1]] = sparkle_img[mask[0], mask[1]]
    return ret

if __name__ == "__main__":
    img_path = sys.argv[1]
    frame = cv2.imread(img_path)
    effected = sparkle(frame)
    while True:
        cv2.imshow("sparkle", effected)
        k = cv2.waitKey(1)
        if k == ord("q"):
            break

    cv2.destroyAllWindows()