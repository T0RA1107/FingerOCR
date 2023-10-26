import cv2
import numpy as np
from Effect.SampleEffect import Effect
from Effect.pumpkin import pumpkin

name2effect = {
    'pumpkin': pumpkin
}

def main():
    cap = cv2.VideoCapture(1)
    effect_type = None
    n_data = 0
    while True:
        ret, frame = cap.read()
        if effect_type is not None:
            Effect = name2effect[effect_type]
            effected = Effect(frame)
            cv2.imshow('camera', effected)
        else:
            cv2.imshow('camera', frame)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break
        elif k == ord('s'):
            cv2.imwrite(f"./test_image/{n_data}.jpg", frame)
        elif k == ord('k'):
            effect_type = 'pumpkin'

if __name__ == "__main__":
    main()
