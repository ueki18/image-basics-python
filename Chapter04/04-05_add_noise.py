import cv2
import numpy as np

img = cv2.imread("input.png")
img_noise = img.copy()

# ノイズを加える画素数の割合
amount = 0.02
num_pixels = int(amount * img.shape[0] * img.shape[1])

# 白い点（塩）を追加
coords = [np.random.randint(0, i, num_pixels) for i in img.shape[:2]]
img_noise[coords[0], coords[1]] = 255

# 黒い点（ごま）を追加
coords = [np.random.randint(0, i, num_pixels) for i in img.shape[:2]]
img_noise[coords[0], coords[1]] = 0

cv2.imwrite("noise.png", img_noise)
