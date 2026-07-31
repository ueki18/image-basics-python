import cv2
import numpy as np

image = cv2.imread("cityscape.png")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
hue = hsv[:, :, 0].astype(np.int32)  # 元のHueをint32で保持

hue_shift = 0

while True:
    hsv[:, :, 0] = ((hue + hue_shift) % 180).astype(np.uint8)
    hue_shift = (hue_shift + 1) % 180

    shifted_image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    cv2.imshow("Hue Shift Animation", shifted_image)

    if cv2.waitKey(30) == 27:
        break

cv2.destroyAllWindows()
