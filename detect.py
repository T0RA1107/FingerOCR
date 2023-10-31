# ライブラリのインポート
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# 色の範囲
# HSVRange["blue"]["lower"]で値を取り出せる
HSVRange = {
    "blue": {"lower": np.array([100, 50, 50]), "upper": np.array([120, 255, 255])},
    "green": {"lower": np.array([50, 50, 50]), "upper": np.array([60, 255, 255])},
    "pink": {"lower": np.array([160, 50, 50]), "upper": np.array([170, 255, 255])},
}

# 実行
while True:
    # -----------以下記述-----------
    #Webカメラのフレーム取得
    ret, frame = cap.read()
    cv2.imshow("camera", frame)
    # 画像をRGBからHSVに変換
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # HSVによる上限、下限の設定　 ([Hue, Saturation, Value])
    hsvLower = np.array([100, 60, 60])  # 下限
    hsvUpper = np.array([120, 255, 255])  # 上限

    # HSVからマスクを作成
    hsv_mask = cv2.inRange(hsv, hsvLower, hsvUpper)

    # medianblurを用いてノイズ成分を除去
    blur_mask = cv2.medianBlur(hsv_mask, ksize=3)

    """
    ここからラベリングを行う
    """
    # ラベリング結果書き出し用に二値画像をカラー変換 (枠や座標をカラー表示したい！)
    src = cv2.cvtColor(blur_mask, cv2.COLOR_GRAY2BGR)

    # ラベリング処理
    nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(blur_mask)

    # 領域(stats[:, 4])が3つ以上ある場合(そのうち1つは背景)だけ処理
    if nlabels >= 3:
        # 面積でソート(今回は面積が上位２つの領域を利用)
        top_idx = stats[:, 4].argsort()[-3:-1]

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
            
            cv2.circle(src, center=(xx, yy), radius=r, color=(0, 0, 255), thickness=5)

            # 領域の重心座標、サイズを表示 (引数 : 描画画像、 書き込む文字列、 書き込む座標、 フォント、 サイズ、 色、 太さ)
            cv2.putText(
                src,
                "Center X: " + str(int(centroids[i, 0])),
                (x1 - 30, y1 + 15),
                cv2.FONT_HERSHEY_PLAIN,
                1,
                (0, 255, 255),
                2,
            )
            cv2.putText(
                src,
                "Center Y: " + str(int(centroids[i, 1])),
                (x1 - 30, y1 + 30),
                cv2.FONT_HERSHEY_PLAIN,
                1,
                (0, 255, 255),
                2,
            )
            cv2.putText(
                src,
                "Size: " + str(int(stats[i, 4])),
                (x1 - 30, y1 + 45),
                cv2.FONT_HERSHEY_PLAIN,
                1,
                (0, 255, 255),
                2,
            )

    # 結果画像の表示
    cv2.imshow("output", src)



    # 終了オプション
    k = cv2.waitKey(1)
    if k == ord("q"):
        break


# カメラリリース、windowの開放
cap.release()
cv2.destroyAllWindows()
