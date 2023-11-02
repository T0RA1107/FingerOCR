import sys
import cv2
import copy
import numpy as np

def chopper(frame):
    ret = copy.deepcopy(frame)
    chopper_image=cv2.imread("./Effect/effect_data/R.png")
    h,w,_ = chopper_image.shape
    grass_img=cv2.imread("./test_image/22.jpg")
    H,W,_ = ret.shape
    mask = np.where(np.any(chopper_image > 0, axis=2))
    ret[H//2-h//2:H//2+h//2, :w, :][mask[0], mask[1]] = chopper_image[mask[0], mask[1]]
    return ret
    




if __name__ == "__main__":
    img_path = sys.argv[1]
    frame = cv2.imread(img_path)
    print(frame.shape)
    effected = chopper(frame)
    while True:
        cv2.imshow("Effect", effected)
        k = cv2.waitKey(1)
        if k == ord("q"):
            break

    cv2.destroyAllWindows()
