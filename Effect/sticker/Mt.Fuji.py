import sys
import cv2
import numpy as np

def Mt_Fuji(frame):
    Mt_Fuji_img = cv2.imread("./Effect/effect_data/sticker/Mt.Fuji.png")
    h, w, _ = Mt_Fuji_img.shape
    ret = copy.deepcopy(frame)
    mask = np.where(np.any(Mt_Fuji_img > 0, axis=2))
    ret[:h, :w, :][mask[0], mask[1]] = Mt_Fuji_img[mask[0], mask[1]]
    return ret

if __name__ == "__main__":
    img_path = sys.argv[1]
    frame = cv2.imread(img_path)
    effected = Mt_Fuji(frame)
    while True:
        cv2.imshow("Mt.Fuji", effected)
        k = cv2.waitKey(1)
        if k == ord("q"):
            break

    cv2.destroyAllWindows()