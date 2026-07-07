import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

# コントラストを1.5倍にする
img_high_contrast = cv2.convertScaleAbs(img, alpha=1.5, beta=0)
# コントラストを半分(0.5倍)にする
img_low_contrast  = cv2.convertScaleAbs(img, alpha=0.5, beta=0)

cv2.imwrite("high_contrast.png", img_high_contrast)
cv2.imwrite("low_contrast.png",  img_low_contrast)

# トーンカーブの描画
x = np.arange(256)
plt.plot(x, np.clip(1.5 * x, 0, 255), linestyle="-",  label="a=1.5 (higher contrast)")
plt.plot(x, np.clip(0.5 * x, 0, 255), linestyle="--", label="a=0.5 (lower contrast)")
plt.plot(x, x,                        linestyle=":",  label="no change")
plt.xlabel("Input")
plt.ylabel("Output")
plt.legend()
plt.savefig("tone_curve_contrast.png")
plt.show()
