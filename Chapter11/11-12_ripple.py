# 11-12_ripple.py
# クリックした位置から波紋が広がるリップル効果

import cv2
import numpy as np

width, height = 640, 480
image = np.ones((height, width, 3), dtype=np.uint8) * 255
window_name = "Ripple Effect"

def draw_ripple(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # 左クリックされたとき
        for i in range(0, 100, 5):
            color_value = min(255, i * 3)  # iが大きいほど白に近づく
            cv2.circle(image, (x, y), i, (color_value, color_value, 255), 2)
            cv2.imshow(window_name, image)
            cv2.waitKey(30)

cv2.namedWindow(window_name)
cv2.setMouseCallback(window_name, draw_ripple)

while True:
    cv2.imshow(window_name, image)
    if cv2.waitKey(30) == 27:
        break

cv2.destroyAllWindows()
