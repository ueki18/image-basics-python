import cv2

img = cv2.imread("input.png")

# 5x5の平均化フィルタ
img_blur_5  = cv2.blur(img, ksize=(5, 5))

# 15x15の平均化フィルタ
img_blur_15 = cv2.blur(img, ksize=(15, 15))

cv2.imwrite("mean_5x5.png",  img_blur_5)
cv2.imwrite("mean_15x15.png", img_blur_15)
