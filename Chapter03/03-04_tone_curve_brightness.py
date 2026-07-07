import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

# 明るくする (+50)，暗くする (-50)
img_bright = cv2.add(img, 50)
img_dark = cv2.subtract(img, 50)
cv2.imwrite("bright.png", img_bright)
cv2.imwrite("dark.png", img_dark)

# トーンカーブの描画
x = np.arange(256)
plt.plot(x, np.clip(x + 50, 0, 255), linestyle="-",  label="C=+50 (brighter)")
plt.plot(x, np.clip(x - 50, 0, 255), linestyle="--", label="C=-50 (darker)")
plt.plot(x, x,                       linestyle=":",  label="no change")
plt.xlabel("Input")
plt.ylabel("Output")
plt.legend()
plt.savefig("tone_curve_offset.png")
plt.show()
