import cv2
import numpy as np

height, width = 128, 256   # 高さ，幅の順で指定
img = np.zeros((height, width), np.uint8)  # グレースケール画像を作成
for y in range(height):
    for x in range(width):
        img[y, x] = x  # x座標の値をそのまま画素値にする（0〜255）
cv2.imwrite("gradation.png", img)
