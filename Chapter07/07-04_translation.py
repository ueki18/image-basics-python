import cv2
import numpy as np

img = cv2.imread("bear.png")
h, w = img.shape[:2]

# X方向に50ピクセル，Y方向に30ピクセル移動する行列
M = np.float32([[1, 0, 50], [0, 1, 30]])

# warpAffineの第3引数は出力画像のサイズ (幅, 高さ)
shifted = cv2.warpAffine(img, M, (w, h))

cv2.imwrite("translation.png", shifted)
