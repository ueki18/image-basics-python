import cv2
import numpy as np
import matplotlib.pyplot as plt

# 画像の読み込み（BGR順）
img_bgr = cv2.imread("landscape.png")
# 表示用にRGB順に変換
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# R, G, B チャンネルに分離 (cv2.splitは元のチャンネル順で返す)
b, g, r = cv2.split(img_bgr)

# matplotlib で並べて表示
fig, axs = plt.subplots(1, 4, figsize=(16, 4))
axs[0].imshow(img_rgb); axs[0].set_title('Original'); axs[0].axis('off')
axs[1].imshow(r, cmap='gray', vmin=0, vmax=255); axs[1].set_title('Red'); axs[1].axis('off')
axs[2].imshow(g, cmap='gray', vmin=0, vmax=255); axs[2].set_title('Green'); axs[2].axis('off')
axs[3].imshow(b, cmap='gray', vmin=0, vmax=255); axs[3].set_title('Blue'); axs[3].axis('off')
plt.show()
