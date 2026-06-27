import cv2

img = cv2.imread("bear.png")
h, w = img.shape[:2]

# 出力サイズを (幅, 高さ) で直接指定（縦横2倍に拡大）
img_big = cv2.resize(img, (2*w, 2*h), interpolation=cv2.INTER_CUBIC)

cv2.imwrite("resize2.png", img_big)
