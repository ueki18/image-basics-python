import cv2
import numpy as np

# 画像の読み込み
img = cv2.imread("objects.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ノイズを低減するために平滑化
gray = cv2.medianBlur(gray, 5)

# 円の検出
# dp: 投票空間の解像度の逆比
# minDist: 検出する円同士の最小距離
# param1: Canny法の高いしきい値
# param2: 円とみなすための最小の投票数
# minRadius: 検出する円の最小半径
# maxRadius: 検出する円の最大半径
circles = cv2.HoughCircles(
    gray,
    cv2.HOUGH_GRADIENT,
    dp=1,
    minDist=25,
    param1=50,
    param2=30,
    minRadius=10,
    maxRadius=30
)

# 検出した円を描画
if circles is not None:
    circles = np.uint16(np.around(circles))
    for circle in circles[0]:
        x, y, r = circle

        # 円の輪郭を緑色で描画
        cv2.circle(img, (x, y), r, (0, 255, 0), 2)

        # 円の中心を赤色で描画
        cv2.circle(img, (x, y), 2, (0, 0, 255), 3)

# 結果を保存
cv2.imwrite("hough_circles.png", img)
