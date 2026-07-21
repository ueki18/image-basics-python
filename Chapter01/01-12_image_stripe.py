import cv2
import numpy as np

height, width = 192, 256
img = np.zeros((height, width, 3), np.uint8)  # カラー画像を作成
for y in range(height):
    for x in range(width):
        if y < 64:
            img[y, x] = [255, 0, 0]    # 青（BGR順）
        elif y < 128:
            img[y, x] = [0, 255, 0]    # 緑
        else:
            img[y, x] = [0, 0, 255]    # 赤
cv2.imwrite("stripe.png", img)
