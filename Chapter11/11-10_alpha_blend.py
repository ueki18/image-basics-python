import cv2

# 同じサイズの2枚の画像を読み込む
img1 = cv2.imread("apple.png")
img2 = cv2.imread("orange.png")

# alpha: img1 の重み（0.0〜1.0）
# 1 - alpha: img2 の重み
alpha = 0.6

# cv2.addWeighted(src1, alpha, src2, beta, gamma)
# 出力 = src1 * alpha + src2 * beta + gamma
img_blend = cv2.addWeighted(img1, alpha, img2, 1.0 - alpha, 0.0)

cv2.imwrite("blend_06.jpg", img_blend)
