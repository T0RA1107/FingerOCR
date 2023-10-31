import sys
import cv2
import numpy as np
import copy

def water(frame):
    water_img = cv2.imread("./Effect/effect_data/drop.png")
    h, w, _ = water_img.shape
    print(water_img[0][0])
    ret = copy.deepcopy(frame)
    mask = np.where(np.any(water_img > 0, axis=2))
    ret[:h, :w, :][mask[0], mask[1]] = water_img[mask[0], mask[1]]
    return ret

if __name__ == "__main__":
    img_path = sys.argv[1]
    frame = cv2.imread(img_path)
    effected = water(frame)
    while True:
        cv2.imshow("water", effected)
        k = cv2.waitKey(1)
        if k == ord("q"):
            break

    cv2.destroyAllWindows()

