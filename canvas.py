import numpy as np
import cv2

class Canvas:
    def __init__(self, h, w):
        self.h = h
        self.w = w
        self.canvas = np.zeros((self.h, self.w, 3), dtype=np.uint8)

    def write(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # カメラの画像をうけとってシールの重心を認識しcanvasに書き込む
        #HSVによる上限と下限の設定
        hsv_Lower = np.array([82,87,85])#下限
        hsv_Upper = np.array([140,216,139])#上限
        #HSVからマスク作成
        hsv_mask = cv2.inRange(hsv,hsv_Lower,hsv_Upper)
        #medianblurを用いてノイズ成分を除去する。
        blur_mask = cv2.medianBlur(hsv_mask,ksize=3)
        #ラベリング処理
        src = cv2.cvtColor(blur_mask,cv2.COLOR_GRAY2BGR)
        new_point = np.zeros_like(src, dtype=np.uint8)
        nlabels, labels, stats, centroid = cv2.connectedComponentsWithStats(blur_mask)

        # 領域(stats[:, 4])が2つ以上ある場合(そのうち1つは背景)だけ処理
        if nlabels >= 2:
            # 面積でソート(今回は面積が上位２つの領域を利用)
            top_idx = stats[:, 4].argsort()[-2]
            cv2.circle(new_point, center=(int(centroid[top_idx, 0]), int(centroid[top_idx, 1])), radius=20, color=(0, 0, 255), thickness=-1)

        self.canvas |= new_point

    def reset(self):
        self.canvas = np.zeros((self.h, self.w, 3), dtype=np.uint8)

    def show(self, frame):
        mask = np.where(self.canvas[:, :, 2] == 255)
        frame[mask[0], mask[1], :] = self.canvas[mask[0], mask[1]]
        cv2.imshow("canvas", frame)
        cv2.moveWindow("canvas", 400, 0)
