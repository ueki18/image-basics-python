import cv2
import numpy as np

noisy_img = cv2.imread("noisy_img.png", cv2.IMREAD_GRAYSCALE)
kernel = np.ones((3, 3), dtype=np.uint8)

# iterations を変えて収縮の結果を比較する
erosion_1 = cv2.erode(noisy_img, kernel, iterations=1)
erosion_2 = cv2.erode(noisy_img, kernel, iterations=2)
erosion_3 = cv2.erode(noisy_img, kernel, iterations=3)

cv2.imwrite("erosion_iter1.png", erosion_1)
cv2.imwrite("erosion_iter2.png", erosion_2)
cv2.imwrite("erosion_iter3.png", erosion_3)
