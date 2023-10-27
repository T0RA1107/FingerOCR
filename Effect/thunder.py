import sys
import cv2
import numpy as np
import copy

def thunder_capture():
    return cv2.VideoCapture("./Effect/effect_data/thunder_04.mp4")

def thunder(frame, thunder_image):
    ret = copy.deepcopy(frame)
    h, w, _ = thunder_image.shape
    mask = np.where(np.any(thunder_image > 50, axis=2))
    ret[:h, :w, :][mask[0], mask[1]] = thunder_image[mask[0], mask[1]]
    return ret

if __name__ == "__main__":
    img_path = sys.argv[1]
    frame = cv2.imread(img_path)
    cap = cv2.VideoCapture("./Effect/effect_data/thunder_04.mp4")
    while True:
        is_ok, thunder_image = cap.read()
        if not is_ok:
            break
        ret = copy.deepcopy(frame)
        h, w, _ = thunder_image.shape
        mask = np.where(np.any(thunder_image > 50, axis=2))
        ret[:h, :w, :][mask[0], mask[1]] = thunder_image[mask[0], mask[1]]
        cv2.imshow("Effect", ret)
        k = cv2.waitKey(1)
        if k == ord("q"):
            break

    cv2.destroyAllWindows()