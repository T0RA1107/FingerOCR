import sys
import cv2
import numpy as np
import copy

def shachihoko(frame):
    ret = copy.deepcopy(frame)
    shachihoko_image = cv2.imread("./Effect/effect_data/sticker/shachihoko.png")
    height, width, channels = shachihoko_image.shape[:3]
    print("width: " + str(width))
    print("height: " + str(height))
    shachihoko_image = cv2.resize(shachihoko_image, (400, 372))
    h, w, _ = shachihoko_image.shape
    mask = np.where(np.any(shachihoko_image > 0, axis=2))
    ret[:h, :w, :][mask[0], mask[1]] = shachihoko_image[mask[0], mask[1]]
    return ret

if __name__ == "__main__":
    img_path = sys.argv[1]
    frame = cv2.imread(img_path)
    effected = shachihoko(frame)
    while True:
        cv2.imshow("Effect", effected)
        k = cv2.waitKey(1)
        if k == ord("q"):
            break

    cv2.destroyAllWindows()