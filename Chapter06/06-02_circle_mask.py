import cv2
import numpy as np

# 元画像を読み込み
img_src = cv2.imread("cat.png")
h, w = img_src.shape[:2]

# 円形マスクをプログラムで生成する
# まず全体を黒（0）で初期化した画像を用意する
img_mask = np.zeros((h, w), dtype=np.uint8)

# 画像の中心を円の中心，短辺の半分を半径として白い円を描く
center = (w // 2, h // 2)
radius = min(w, h) // 2
cv2.circle(img_mask, center, radius, 255, thickness=-1)  # thickness=-1で塗りつぶし

# マスクの白い部分だけを元画像から抽出する
img_dst = cv2.bitwise_and(img_src, img_src, mask=img_mask)

cv2.imwrite("circle_mask.png", img_mask)
cv2.imwrite("cat_circle.jpg", img_dst)
