import cv2
import numpy as np

# 画像の読み込み
img = cv2.imread("book_coins.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ノイズを低減するために平滑化
gray = cv2.GaussianBlur(gray, (5, 5), 0)

# Canny法によるエッジ検出
# 第2引数: 低いしきい値
# 第3引数: 高いしきい値
edges = cv2.Canny(gray, 100, 200)

# 確率的ハフ変換による直線検出
# rho: 距離方向の分解能（画素）
# theta: 角度方向の分解能（ラジアン）
# threshold: 直線とみなすための最小の交点（投票）数
# minLineLength: 検出する直線の最小の長さ
# maxLineGap: 同一の線とみなす、点と点の間隔の最大値
lines = cv2.HoughLinesP(
    edges,
    rho=1,
    theta=np.pi / 180,
    threshold=60,
    minLineLength=60,
    maxLineGap=10
)

# 検出した直線を赤色で描画
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

# 結果を保存
cv2.imwrite("hough_lines.png", img)
