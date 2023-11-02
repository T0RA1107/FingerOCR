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
        hsv_Lower = np.array([100,60,60])#下限
        hsv_Upper = np.array([120,255,255])#上限
        #HSVからマスク作成
        hsv_mask = cv2.inRange(hsv,hsv_Lower,hsv_Upper)
        #medianblurを用いてノイズ成分を除去する。
        blur_mask = cv2.medianBlur(hsv_mask,ksize=3)
        #ラベリング処理
        src = cv2.cvtColor(blur_mask,cv2.COLOR_GRAY2BGR)
        new_point = np.zeros_like(src, dtype=np.uint8)
        nlabels, labels, stats, centroid = cv2.connectedComponentsWithStats(blur_mask)
        # 領域(stats[:, 4])が3つ以上ある場合(そのうち1つは背景)だけ処理
        if nlabels >= 3:
            # 面積でソート(今回は面積が上位２つの領域を利用)
            top_idx = stats[:, 4].argsort()[-2:-1]

            # 各領域において...
            for i in top_idx:

                # 領域の外接矩形の角座標を入手
                x0 = stats[i, 0]
                y0 = stats[i, 1]
                x1 = x0 + stats[i, 2]
                y1 = y0 + stats[i, 3]
                xx = (x1 + x0)//2
                yy = (y1 + y0)//2
                r = (x1 - x0)//2
                
                cv2.circle(new_point, center=(xx, yy), radius=8, color=(0, 0, 255), thickness=-1)
            
        self.canvas |= new_point
    
    def reset(self):
        self.canvas = np.zeros((self.h, self.w, 3), dtype=np.uint8)
    
    def show(self, frame):
        mask = np.where(self.canvas[:, :, 2] == 255)
        frame[mask[0], mask[1], :] = self.canvas[mask[0], mask[1]]
        cv2.imshow("canvas", frame)
