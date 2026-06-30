import numpy as np
import cv2

img1_color = cv2.imread("left.png")              # カラーで読み込み
img2_color = cv2.imread("right.png")
img1_gray = cv2.cvtColor(img1_color, cv2.COLOR_BGR2GRAY)  # 検出用にグレースケール変換
img2_gray = cv2.cvtColor(img2_color, cv2.COLOR_BGR2GRAY)

# SIFTで特徴点と記述子を抽出（グレースケール画像を使用）
sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1_gray, None)
kp2, des2 = sift.detectAndCompute(img2_gray, None)

# FLANNによる高速マッチング
index_params = dict(algorithm=1, trees=5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1, des2, k=2)

# レシオテスト
good_matches = [m for m, n in matches if m.distance < 0.75 * n.distance]

# 対応点の座標を取得
src_pts = np.float32(
    [kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
dst_pts = np.float32(
    [kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

# RANSACでホモグラフィ行列を推定（許容誤差5.0ピクセル）
H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

# img1の四隅がHでどこに写るか計算し、はみ出し量を求める
h, w = img1_gray.shape
corners = np.float32([[0, 0], [w, 0], [w, h], [0, h]]).reshape(-1, 1, 2)
warped_corners = cv2.perspectiveTransform(corners, H)
x_min = warped_corners[:, 0, 0].min()
x_max = warped_corners[:, 0, 0].max()

# はみ出す分だけ右にずらす平行移動行列を作る
shift = max(0, -x_min)
T = np.array([[1, 0, shift],
              [0, 1, 0],
              [0, 0, 1]], dtype=np.float64)

# 平行移動を合成したホモグラフィでimg1（カラー）を変換
canvas_w = int(max(x_max, img2_color.shape[1]) + shift) + 5
result = cv2.warpPerspective(img1_color, T @ H, (canvas_w, img1_color.shape[0]))

# img2（カラー）もずらした位置に貼り付ける
result[0:img2_color.shape[0], int(shift):int(shift) + img2_color.shape[1]] = img2_color

# 黒い余白をトリミング（上下左右）
gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
rows = np.where(np.any(gray != 0, axis=1))[0]
cols = np.where(np.any(gray != 0, axis=0))[0]
margin = 10  # 端の歪みを避けるための余白カット
result_final = result[rows.min()+margin:rows.max()+1-margin,
                       cols.min()+margin:cols.max()+1-margin]

cv2.imwrite("panorama.png", result_final)
