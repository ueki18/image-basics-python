import cv2

# 画像の読み込み
img = cv2.imread("input.png")

# バイラテラルフィルタ
# 第2引数: 対象となる領域の直径 (d)
# 第3引数: 色空間の標準偏差
# 第4引数: 距離空間の標準偏差
img_bilateral = cv2.bilateralFilter(
    img,
    d=9,
    sigmaColor=75,
    sigmaSpace=75
)

# 結果を保存
cv2.imwrite("bilateral.png", img_bilateral)
