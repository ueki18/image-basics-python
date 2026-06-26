import cv2

img = cv2.imread("cityscape.png", cv2.IMREAD_GRAYSCALE)

# ノイズの影響を抑えるため事前に平滑化
img_blur = cv2.GaussianBlur(img, (3, 3), 0)

# Laplacianフィルタの適用
laplacian = cv2.Laplacian(img_blur, cv2.CV_64F, ksize=3)

# 8ビット画像へ変換
laplacian = cv2.convertScaleAbs(laplacian)

cv2.imwrite("laplacian.png", laplacian)
