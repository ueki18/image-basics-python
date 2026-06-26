import cv2

img = cv2.imread("cityscape.png", cv2.IMREAD_GRAYSCALE)

# X方向の微分（縦方向のエッジを抽出）
sobel_x = cv2.Sobel(img, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=3)

# Y方向の微分（横方向のエッジを抽出）
sobel_y = cv2.Sobel(img, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=3)

# 勾配の大きさ（マグニチュード）を計算
sobel_mag = cv2.magnitude(sobel_x, sobel_y)

# 8ビット画像へ変換
sobel_mag = cv2.convertScaleAbs(sobel_mag)

cv2.imwrite("sobel.png", sobel_mag)
