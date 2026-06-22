import cv2
import numpy as np
img = cv2.imread("sample.jpg")

# 方法1: cv2.add()（飽和演算：255を超えた値は255に丸められる）
bright1 = cv2.add(img, np.full(img.shape, 50, dtype=np.uint8))

# 方法2: np.clip()（int16に変換してから加算し，クリップして戻す）
bright2 = np.clip(img.astype(np.int16) + 50, 0, 255).astype(np.uint8)

cv2.imwrite("bright_cv2add.jpg", bright1)
cv2.imwrite("bright_clip.jpg", bright2)
