import cv2
import numpy as np

size = 400      # 画像サイズ（正方形）
cell = 50       # 1マスのサイズ（ピクセル）
img = np.zeros((size, size), np.uint8)
for y in range(size):
    for x in range(size):
        if (y // cell + x // cell) % 2 == 0:
            img[y, x] = 255   # 白
        else:
            img[y, x] = 0     # 黒
cv2.imwrite("checker.png", img)
