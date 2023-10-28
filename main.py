import cv2
import numpy as np
import glob
import os
import subprocess
from playsound import playsound
from Effect.EffectController import EffectController

save_dir = "./test_image"

def main():
    cap = cv2.VideoCapture(1)
    effect_controller = EffectController()
    n_data = len(glob.glob(os.path.join(save_dir, "[0-9]*.jpg")))
    while True:
        ret, frame = cap.read()
        frame = frame[:, ::-1, :]
        effected = effect_controller.effect(frame)
        cv2.imshow('camera', effected)
        k = cv2.waitKey(1)
        if k == ord('q') or not ret:
            break
        elif k == ord('s'):
            cv2.imwrite(f"./test_image/{n_data}.jpg", effected)
            playsound("./Sound/Camera-Film03-1.mp3")
        elif k == ord('r'):
            effect_controller.reset()
        elif k == ord('p'):
            effect_controller.set_effect("pumpkin")
        elif k == ord('t'):
            effect_controller.set_effect("thunder")
        elif k == ord('w'):
            print('pushing')

if __name__ == "__main__":
    main()
