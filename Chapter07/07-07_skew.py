import cv2
import numpy as np
import math

img = cv2.imread("bear.png")
h, w = img.shape[:2]

# X軸方向に20度のせん断変形
theta = math.radians(20)

M_skew = np.float32([
    [1, math.tan(theta), 0],
    [0, 1,               0]
])

# 横幅が広がる分，出力画像のサイズを調整
new_w = w + int(h * math.tan(theta))
skewed = cv2.warpAffine(img, M_skew, (new_w, h))

cv2.imwrite("skewed.png", skewed)
