import cv2
import numpy as np

cap = cv2.VideoCapture("sample_video.mp4")
ret, frame1 = cap.read()
prev_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

# 可視化用のHSV画像を準備（彩度は常に最大値にしておく）
hsv = np.zeros_like(frame1)
hsv[..., 1] = 255

while True:
    ret, frame2 = cap.read()
    if not ret:
        break
    next_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # 全画素の移動ベクトル(dx, dy)を計算
    flow = cv2.calcOpticalFlowFarneback(
        prev_gray, next_gray, None,
        pyr_scale=0.5, levels=3, winsize=15,
        iterations=3, poly_n=5, poly_sigma=1.2, flags=0)

    # ベクトル(dx, dy)を大きさ(mag)と角度(ang)に変換
    mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])

    # 角度を色相(0-179)に，大きさを明度(0-255)に正規化して反映
    # OpenCVのHueは8bit(0-179)で360度を表現するため，度数法の角度(0-360)を2で割る
    hsv[..., 0] = ang * 180 / np.pi / 2
    hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)

    # HSVをBGRに変換して表示
    bgr_flow = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    cv2.imshow("Dense Optical Flow", bgr_flow)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

    prev_gray = next_gray

cap.release()
cv2.destroyAllWindows()
