import cv2
import numpy as np
import glob
import os
import time
from playsound import playsound
import threading
from Effect.EffectController import EffectController
from canvas import Canvas

save_dir = "./test_image"

def main():
    cap = cv2.VideoCapture(0)
    effect_controller = EffectController()
    H = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    W = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    canvas = Canvas(H, W)
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
            cv2.imwrite(f"{save_dir}/{n_data}.jpg", effected)
            threading.Thread(target=playsound, args=("./Sound/Camera/Camera-Film03-1.mp3",)).start()
            n_data += 1
        elif k == ord('r'):
            effect_controller.reset()
        elif k == ord('w'):
            canvas.write(frame)
        elif k == ord('i'):
            st = time.time()
            text = effect_controller.recognize_finger_writing(canvas.canvas)
            inf_t = time.time() - st
            print("inference time: {:.2}".format(inf_t))
            print("Predict:", text)
            if effect_controller.is_effect(text):
                effect_controller.set_effect(text)
            canvas.reset()
        elif k== ord('c'):
            canvas.reset()
        canvas.show(frame)

if __name__ == "__main__":
    main()
