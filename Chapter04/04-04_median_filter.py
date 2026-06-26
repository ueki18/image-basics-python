import cv2

# 画像の読み込み
img = cv2.imread("input.png")

# 中央値フィルタ
# ksize: カーネルサイズ（3, 5, 7などの奇数）
img_median = cv2.medianBlur(img, ksize=5)

# 結果を保存
cv2.imwrite("median.png", img_median)
