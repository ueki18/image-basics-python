import cv2
import numpy as np

# 背景画像（人物や車がいない状態）を読み込む
img_bg = cv2.imread("background.jpg")
# 観測画像（移動物体が含まれる状態）を読み込む
img_obs = cv2.imread("observed.jpg")

# 絶対差分を計算（各画素で |観測 - 背景| を求める）
img_diff = cv2.absdiff(img_obs, img_bg)

# 差分画像をグレースケールに変換してからしきい値処理で二値化
img_diff_gray = cv2.cvtColor(img_diff, cv2.COLOR_BGR2GRAY)
_, img_mask = cv2.threshold(img_diff_gray, 30, 255, cv2.THRESH_BINARY)

# モルフォロジー演算でノイズを除去し，マスクを整形する
kernel = np.ones((5, 5), np.uint8)
img_mask = cv2.morphologyEx(img_mask, cv2.MORPH_OPEN, kernel)
img_mask = cv2.morphologyEx(img_mask, cv2.MORPH_CLOSE, kernel)

# マスクを使って観測画像から前景だけを切り出す
img_fg = cv2.bitwise_and(img_obs, img_obs, mask=img_mask)

cv2.imwrite("diff.jpg", img_diff)
cv2.imwrite("mask.jpg", img_mask)
cv2.imwrite("foreground.jpg", img_fg)
