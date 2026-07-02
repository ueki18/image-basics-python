import cv2
import numpy as np

width, height = 640, 480
image = np.ones((height, width, 3), dtype=np.uint8) * 255

size = 50   # 矩形の初期サイズ
delta = 2   # サイズの変化量

while True:
    image[:] = 255

    top_left = (width // 2 - size // 2, height // 2 - size // 2)
    bottom_right = (width // 2 + size // 2, height // 2 + size // 2)
    cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), -1)

    size += delta
    if size > 200 or size < 50:  # サイズの上限・下限に達したら向きを反転
        delta = -delta

    cv2.imshow("Scaling Rectangle", image)
    if cv2.waitKey(30) == 27:
        break

cv2.destroyAllWindows()
