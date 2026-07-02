# 11-11_dissolve.py
# アルファ値を段階的に変化させたディゾルブ効果

import cv2
import numpy as np

img1 = cv2.imread("apple.jpg")
img2 = cv2.imread("orange.jpg")

# alpha を 0.0, 0.2, 0.4, 0.6, 0.8, 1.0 の6段階で変化させる
alphas = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
frames = []

for alpha in alphas:
    blended = cv2.addWeighted(img1, alpha, img2, 1.0 - alpha, 0.0)
    frames.append(blended)

# 6枚の合成画像を横に並べて1枚の比較画像として保存
comparison = np.hstack(frames)
cv2.imwrite("dissolve_comparison.jpg", comparison)
