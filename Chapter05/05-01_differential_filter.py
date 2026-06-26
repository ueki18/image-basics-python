import numpy as np
import cv2

img = cv2.imread("cityscape.png", cv2.IMREAD_GRAYSCALE)

# 横方向（x方向）中心差分
op_x = 0.5 * np.array([[0, 0, 0],
                       [-1, 0, 1],
                       [0, 0, 0]], dtype=np.float32)

img_diff_x = cv2.filter2D(img, ddepth=cv2.CV_32F, kernel=op_x)
img_diff_x = cv2.convertScaleAbs(img_diff_x)
img_diff_x = cv2.normalize(img_diff_x, None, 0, 255, cv2.NORM_MINMAX)

# 縦方向（y方向）中心差分
op_y = 0.5 * np.array([[0, -1, 0],
                       [0,  0, 0],
                       [0,  1, 0]], dtype=np.float32)

img_diff_y = cv2.filter2D(img, ddepth=cv2.CV_32F, kernel=op_y)
img_diff_y = cv2.convertScaleAbs(img_diff_y)
img_diff_y = cv2.normalize(img_diff_y, None, 0, 255, cv2.NORM_MINMAX)

cv2.imwrite("diff_x.png", img_diff_x)
cv2.imwrite("diff_y.png", img_diff_y)
