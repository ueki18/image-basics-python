import cv2

img = cv2.imread("bear.png")

# 第2引数（flipCode）: 0は上下反転，正の値（例: 1）は左右反転，負の値（例: -1）は上下左右両方の反転
img_flip_vertical   = cv2.flip(img, 0)   # 上下反転
img_flip_horizontal = cv2.flip(img, 1)   # 左右反転
img_flip_both       = cv2.flip(img, -1)  # 上下左右反転

cv2.imwrite("flip_vertical.png",   img_flip_vertical)
cv2.imwrite("flip_horizontal.png", img_flip_horizontal)
cv2.imwrite("flip_both.png",       img_flip_both)
