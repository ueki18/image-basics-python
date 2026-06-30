import cv2

img1 = cv2.imread("book.png", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("book_rotated.png", cv2.IMREAD_GRAYSCALE)

# SIFTで特徴点と記述子を抽出
sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# ブルートフォースマッチャーの生成（SIFT はL2距離を使用）
bf = cv2.BFMatcher(cv2.NORM_L2)

# 上位2候補を取得（レシオテスト用）
matches = bf.knnMatch(des1, des2, k=2)

# レシオテストで誤対応を排除
good_matches = []
ratio = 0.75
for m, n in matches:
    if m.distance < ratio * n.distance:
        good_matches.append([m])

# 対応点を線で結んで描画
img_match = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good_matches,
                                None, flags=2)
cv2.imwrite("sift_match.png", img_match)
