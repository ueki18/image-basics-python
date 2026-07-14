import cv2
import numpy as np

img = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

gamma = 1.5
# 高速化のために「ルックアップテーブル(LUT)」を作成
table = np.array([((i / 255.0) ** gamma) * 255
                  for i in np.arange(0, 256)]).astype("uint8")

# LUTを用いて画像全体を一括変換
img_gamma = cv2.LUT(img, table)

cv2.imwrite("gamma.png", img_gamma)
