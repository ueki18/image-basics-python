import cv2
import numpy as np

# 画像の読み込みとHSV変換
img = cv2.imread("landscape.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 青色とみなすHSVの範囲を定義
# Hue（色相）はOpenCVでは0~179の範囲。青はおよそ100~130付近
lower_blue = np.array([100, 50, 50])
upper_blue = np.array([130, 255, 255])

# 指定した範囲に収まる画素を255(白)、それ以外を0(黒)とするマスク画像を作成
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# 元の画像とマスク画像の論理積（AND）をとる
# マスクが白の部分だけ元の色が残り、黒の部分は黒になる
result = cv2.bitwise_and(img, img, mask=mask)

cv2.imwrite("blue_sky_extracted.png", result)
