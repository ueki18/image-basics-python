import cv2

# グレースケールで画像を読み込む
img = cv2.imread("cityscape.png", cv2.IMREAD_GRAYSCALE)

# Canny法のエッジ検出
# 第2引数: threshold1 (低いしきい値)
# 第3引数: threshold2 (高いしきい値)
edges = cv2.Canny(img, 100, 200)

cv2.imwrite("canny.png", edges)
