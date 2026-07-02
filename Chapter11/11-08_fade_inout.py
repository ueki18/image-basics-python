import cv2
import numpy as np

image = cv2.imread("panda.png")

alpha = 0.0
fade_in = True

while True:
    if fade_in:
        alpha += 0.01
        if alpha >= 1.0:
            alpha = 1.0
            fade_in = False
    else:
        alpha -= 0.01
        if alpha <= 0.0:
            alpha = 0.0
            fade_in = True

    # アルファブレンディングにより，元画像と黒画像を合成する
    blended = cv2.addWeighted(image, alpha, np.zeros_like(image), 1 - alpha, 0)

    cv2.imshow("Fade In and Out", blended)
    if cv2.waitKey(30) == 27:
        break

cv2.destroyAllWindows()
