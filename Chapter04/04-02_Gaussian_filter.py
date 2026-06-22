import cv2

img = cv2.imread("input.png")

# 5x5のガウシアンフィルタ（第3引数0: 標準偏差をカーネルサイズから自動計算）
img_gaussian_5  = cv2.GaussianBlur(img, (5, 5),   0)

# 15x15のガウシアンフィルタ
img_gaussian_15 = cv2.GaussianBlur(img, (15, 15), 0)

cv2.imwrite("gaussian_5x5.png",  img_gaussian_5)
cv2.imwrite("gaussian_15x15.png", img_gaussian_15)
