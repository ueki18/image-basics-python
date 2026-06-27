import cv2

img = cv2.imread("bear.png")

# 第2引数（flipCode）: 0は上下反転，正の値（例: 1）は左右反転，負の値（例: -1）は上下左右両方の反転
img_flip_x = cv2.flip(img, 0)   # 上下反転
img_flip_y = cv2.flip(img, 1)   # 左右反転
img_flip_xy = cv2.flip(img, -1) # 上下左右反転

cv2.imwrite("flip_x.png",  img_flip_x)
cv2.imwrite("flip_y.png",  img_flip_y)
cv2.imwrite("flip_xy.png", img_flip_xy)
