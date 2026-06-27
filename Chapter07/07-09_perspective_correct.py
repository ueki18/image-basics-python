import cv2
import numpy as np

img = cv2.imread("bear_distorted.png")
h, w = img.shape[:2]

# 変換前の4点（台形の四隅）※07-08と同じpts2
margin = 100
pts1 = np.float32([
    [margin,      0  ],  # 左上
    [w-1-margin,  0  ],  # 右上
    [0,           h-1],  # 左下
    [w-1,         h-1],  # 右下
])

# 変換後の4点（正面から見た長方形に補正）
pts2 = np.float32([
    [0,   0  ],  # 左上
    [w-1, 0  ],  # 右上
    [0,   h-1],  # 左下
    [w-1, h-1],  # 右下
])

# 4点のペアから透視変換行列を計算して補正を適用
M = cv2.getPerspectiveTransform(pts1, pts2)
corrected = cv2.warpPerspective(img, M, (w, h))

cv2.imwrite("bear_corrected.png", corrected)
