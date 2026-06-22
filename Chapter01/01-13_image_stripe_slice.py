import cv2
import numpy as np

width, height = 256, 192
img = np.zeros((height, width, 3), np.uint8)
img[0:64, :]   = [255, 0, 0]    # 上1/3を青に
img[64:128, :] = [0, 255, 0]    # 中1/3を緑に
img[128:, :]   = [0, 0, 255]    # 下1/3を赤に
cv2.imwrite("stripe_slice.png", img)
