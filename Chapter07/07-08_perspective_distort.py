import cv2
import numpy as np

img = cv2.imread("bear.png")
h, w = img.shape[:2]

# 変換前の4点（元画像の四隅）
pts1 = np.float32([
    [0,   0  ],  # 左上
    [w-1, 0  ],  # 右上
    [0,   h-1],  # 左下
    [w-1, h-1],  # 右下
])

# 変換後の4点（台形状に歪ませる）
margin = 100
pts2 = np.float32([
    [margin,      0  ],  # 左上を右にずらす
    [w-1-margin,  0  ],  # 右上を左にずらす
    [0,           h-1],  # 左下はそのまま
    [w-1,         h-1],  # 右下はそのまま
])

# 4点のペアから透視変換行列を計算して変換を適用
M = cv2.getPerspectiveTransform(pts1, pts2)
distorted = cv2.warpPerspective(img, M, (w, h))

cv2.imwrite("bear_distorted.png", distorted)
