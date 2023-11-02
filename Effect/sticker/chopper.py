import sys
import cv2
import copy
import numpy as np
sys.path.append("./Effect")
from effect_base import EffectBase

def chopper(frame):
    ret = copy.deepcopy(frame)
    chopper_image=cv2.imread("./Effect/effect_data/R.png")
    h,w,_ = chopper_image.shape
    grass_img=cv2.imread("./test_image/22.jpg")
    H,W,_ = ret.shape
    mask = np.where(np.any(chopper_image > 0, axis=2))
    ret[H//2-h//2:H//2+h//2, :w, :][mask[0], mask[1]] = chopper_image[mask[0], mask[1]]
    return ret
    

