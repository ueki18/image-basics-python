import cv2
import numpy as np

img = cv2.imread("cityscape.png", cv2.IMREAD_GRAYSCALE)

# X方向のPrewittカーネル
kernel_x = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
], dtype=np.float32)

# Y方向のPrewittカーネル
kernel_y = np.array([
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
], dtype=np.float32)

prewitt_x = cv2.filter2D(img, cv2.CV_64F, kernel_x)
prewitt_y = cv2.filter2D(img, cv2.CV_64F, kernel_y)

# 勾配の大きさ
prewitt_mag = cv2.magnitude(prewitt_x, prewitt_y)

# 8ビット画像へ変換
prewitt_mag = cv2.convertScaleAbs(prewitt_mag)

cv2.imwrite("prewitt.png", prewitt_mag)
