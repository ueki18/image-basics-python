import cv2
import numpy as np

img = cv2.imread("flower.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 黄色の範囲を指定（Hueは黄色付近の20〜40）
lower = np.array([20, 50, 50])
upper = np.array([40, 255, 255])

# マスク画像を作成し，元画像に適用
mask = cv2.inRange(hsv, lower, upper)
result = cv2.bitwise_and(img, img, mask=mask)

cv2.imwrite("flower_yellow.jpg", result)
