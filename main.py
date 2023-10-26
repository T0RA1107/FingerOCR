import cv2
import numpy as np
from Effect.SampleEffect import Effect

def main():
    cap = cv2.VideoCapture(1)
    is_effect = False
    n_data = 0
    while True:
        ret, frame = cap.read()
        if is_effect:
            effected = Effect(frame)
            cv2.imshow('camera', effected)
        else:
            cv2.imshow('camera', frame)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break
        elif k == ord('e'):
            is_effect ^= True
        elif k == ord('s'):
            cv2.imwrite(f"./test_image/{n_data}.jpg", frame)

if __name__ == "__main__":
    main()
