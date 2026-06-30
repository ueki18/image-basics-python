import cv2

img = cv2.imread("book.png", cv2.IMREAD_GRAYSCALE)

# SIFTのインスタンスを生成
sift = cv2.SIFT_create()

# キーポイントと記述子を同時に検出・算出
kp, des = sift.detectAndCompute(img, None)

# キーポイントを画像上に描画
img_kp = cv2.drawKeypoints(img, kp, None,
                            flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imwrite("sift_kp.png", img_kp)
