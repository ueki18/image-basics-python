import cv2

# 照明ムラのある画像（本のページなど）を読み込み
img = cv2.imread("book_page.png", cv2.IMREAD_GRAYSCALE)

# 固定しきい値（大津の方法）による二値化
_, global_binary = cv2.threshold(
    img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

# 適応的二値化（ガウス加重平均を利用）
# blockSize=21: 周囲21x21ピクセルの領域からしきい値を計算
# C=10: 計算された平均値から10を引いてしきい値を決定
adaptive_binary = cv2.adaptiveThreshold(
    img, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    blockSize=21,
    C=10
)

cv2.imwrite("global_binary.png", global_binary)
cv2.imwrite("adaptive_binary.png", adaptive_binary)
