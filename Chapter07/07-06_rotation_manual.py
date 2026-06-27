import cv2
import numpy as np

img = cv2.imread("bear.png")
h, w = img.shape[:2]

# ラジアンで角度を指定（正の値が反時計回り）
angle = np.pi / 4  # 45度

cx, cy = w / 2, h / 2  # 画像の中心座標

# 変換行列を自分で作成（回転後も中心が中心に来るよう平行移動を調整）
M = np.array([
    [ np.cos(angle), np.sin(angle), cx * (1 - np.cos(angle)) - cy * np.sin(angle)],
    [-np.sin(angle), np.cos(angle), cy * (1 - np.cos(angle)) + cx * np.sin(angle)]
], dtype=np.float32)

rotated2 = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_LINEAR)

cv2.imwrite("rotated2.png", rotated2)
