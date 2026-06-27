import cv2

img = cv2.imread("bear.png")
h, w = img.shape[:2]

# 画像の中心を回転軸として，反時計回りに45度回転，スケールはそのまま(1.0)
center = (w // 2, h // 2)
M_rot = cv2.getRotationMatrix2D(center, 45, 1.0)

rotated = cv2.warpAffine(img, M_rot, (w, h))

cv2.imwrite("rotated.png", rotated)
