import cv2

img = cv2.imread("cityscape.png")

# ボケ画像を作成
blur = cv2.GaussianBlur(img, (9, 9), 10.0)

# cv2.addWeighted で合成 ( src1*alpha + src2*beta + gamma )
# O = 2.0 * img - 1.0 * blur  (k=1.0 の場合)
img_sharp = cv2.addWeighted(img, 2.0, blur, -1.0, 0)

cv2.imwrite("sharp.png", img_sharp)
