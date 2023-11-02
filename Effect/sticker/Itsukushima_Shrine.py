import sys
import cv2
import numpy as np
import copy

def Itsukushima_Shrine(frame):
    ret = copy.deepcopy(frame)
    Itsukushima_Shrine_image = cv2.imread("./Effect/effect_data/sticker/Itsukushima_Shrine.png")
    height, width, channels = Itsukushima_Shrine_image.shape[:3]
    print("width: " + str(width))
    print("height: " + str(height))
    Itsukushima_Shrine_image = cv2.resize(Itsukushima_Shrine_image, (400, 376))
    h, w, _ = Itsukushima_Shrine_image.shape
    mask = np.where(np.any(Itsukushima_Shrine_image > 0, axis=2))
    ret[:h, :w, :][mask[0], mask[1]] = Itsukushima_Shrine_image[mask[0], mask[1]]
    return ret

if __name__ == "__main__":
    img_path = sys.argv[1]
    frame = cv2.imread(img_path)
    effected = Itsukushima_Shrine(frame)
    while True:
        cv2.imshow("Effect", effected)
        k = cv2.waitKey(1)
        if k == ord("q"):
            break

    cv2.destroyAllWindows()