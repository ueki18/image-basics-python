import cv2
import numpy as np

width, height = 640, 480
image = np.ones((height, width, 3), dtype=np.uint8) * 255

# 線を描く
cv2.line(image, (50, 50), (590, 50), (255, 0, 0), 5)  # 青色

# 円を描く（塗りつぶし）
cv2.circle(image, (320, 240), 50, (0, 255, 0), -1)  # 緑色

# 長方形を描く
cv2.rectangle(image, (100, 100), (200, 200), (0, 0, 255), 3)  # 赤色

# 楕円を描く
cv2.ellipse(image, (320, 240), (100, 50), 0, 0, 360, (255, 255, 0), 2)  # シアン

cv2.imshow("Image with Shapes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
