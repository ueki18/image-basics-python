import cv2

# グレースケール画像の読み込み
img = cv2.imread("sample.png", cv2.IMREAD_GRAYSCALE)

# ヒストグラム平坦化を実行
img_eq = cv2.equalizeHist(img)

cv2.imwrite("equalized.png", img_eq)
