import cv2
import numpy as np

noisy_img = cv2.imread("noisy_img.png", cv2.IMREAD_GRAYSCALE)

# 4近傍カーネル（十字型）
kernel_4 = np.array([[0, 1, 0],
                      [1, 1, 1],
                      [0, 1, 0]], dtype=np.uint8)

# 8近傍カーネル（正方形）
kernel_8 = np.ones((3, 3), dtype=np.uint8)

# 膨張（4近傍・8近傍）
dilation_4 = cv2.dilate(noisy_img, kernel_4, iterations=1)
dilation_8 = cv2.dilate(noisy_img, kernel_8, iterations=1)

# 収縮（4近傍・8近傍）
erosion_4 = cv2.erode(noisy_img, kernel_4, iterations=1)
erosion_8 = cv2.erode(noisy_img, kernel_8, iterations=1)

cv2.imwrite("dilation_4.png", dilation_4)
cv2.imwrite("dilation_8.png", dilation_8)
cv2.imwrite("erosion_4.png",  erosion_4)
cv2.imwrite("erosion_8.png",  erosion_8)
