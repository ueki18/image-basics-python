import cv2
import numpy as np

width, height = 640, 480
image = np.ones((height, width, 3), dtype=np.uint8) * 255

x, y = width // 2, height // 2  # 円の初期位置
vx, vy = 5, 5  # x, y方向の速度

while True:
    image[:] = 255
    cv2.circle(image, (x, y), 50, (0, 0, 255), -1)

    x += vx
    y += vy

    # 画面の端で跳ね返る
    if x <= 50 or x >= width - 50:
        vx = -vx
    if y <= 50 or y >= height - 50:
        vy = -vy

    cv2.imshow("Moving Circle", image)
    if cv2.waitKey(30) == 27:
        break

cv2.destroyAllWindows()
