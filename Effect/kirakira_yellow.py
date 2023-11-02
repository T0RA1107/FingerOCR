import sys
import cv2
import numpy as np
import copy

def kirakira_yellow_capture():
    return cv2.VideoCapture("./Effect/effect_data/kirakira_02_yellow.mp4")

def kirakira_yellow(frame, kirakira_yellow_image):
    ret = copy.deepcopy(frame)
    H, W, _ = frame.shape
    h, w, _ = kirakira_yellow_image.shape
    if H < h or W < w:
        rate = min(h / H, w / W)
        kirakira_yellow_image = cv2.resize(kirakira_yellow_image, fx=rate, fy=rate)
    mask = np.where(np.any(kirakira_yellow_image > 50, axis=2))
    ret[:h, :w, :][mask[0], mask[1]] = kirakira_yellow_image[mask[0], mask[1]]
    return ret

if __name__ == "__main__":
    img_path = sys.argv[1]
    frame = cv2.imread(img_path)
    cap = cv2.VideoCapture("./Effect/effect_data/kirakira_02_yellow.mp4")
    while True:
        is_ok, kirakira_yellow_image = cap.read()
        if not is_ok:
            break
        ret = copy.deepcopy(frame)
        h, w, _ = kirakira_yellow_image.shape
        mask = np.where(np.any(kirakira_yellow_image > 50, axis=2))
        ret[:h, :w, :][mask[0], mask[1]] = kirakira_yellow_image[mask[0], mask[1]]
        cv2.imshow("Effect", ret)
        k = cv2.waitKey(1)
        if k == ord("q"):
            break

    cv2.destroyAllWindows()