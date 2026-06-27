import cv2

img = cv2.imread("bear.png")
h, w = img.shape[:2]
print(h, w)  # 元のサイズを確認

# fx, fyで倍率を指定（縦横2倍に拡大）
img_big = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
print(img_big.shape[:2])  # 拡大後のサイズを確認

cv2.imwrite("resize1.png", img_big)
