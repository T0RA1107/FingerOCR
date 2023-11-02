import sys
import cv2
import numpy as np
import copy

def penguin(frame):
    penguin_img = cv2.imread("./Effect/effect_data/sticker/penguin.png")
    height, width, channels = penguin_img.shape[:3]
    print("width: " + str(width))
    print("height: " + str(height))
    penguin_img = cv2.resize(penguin_img, (370, 400))
    h, w, _ = penguin_img.shape
    ret = copy.deepcopy(frame)
    mask = np.where(np.any(penguin_img > 0, axis=2))
    ret[:h, :w, :][mask[0], mask[1]] = penguin_img[mask[0], mask[1]]
    return ret

if __name__ == "__main__":
    img_path = sys.argv[1]
    frame = cv2.imread(img_path)
    effected = penguin(frame)
    while True:
        cv2.imshow("Effect", effected)
        k = cv2.waitKey(1)
        if k == ord("q"):
            break

    cv2.destroyAllWindows()