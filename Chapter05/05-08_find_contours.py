import cv2

# 画像の読み込み
img = cv2.imread("objects.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二値化
# 背景が明るく，物体が暗いため，THRESH_BINARY_INVで物体を白にする
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# 輪郭抽出
# RETR_EXTERNAL: 最も外側の輪郭のみ抽出
# CHAIN_APPROX_SIMPLE: 輪郭を圧縮して頂点のみ保持
contours, hierarchy = cv2.findContours(
    binary,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# 抽出した輪郭を緑色で描画
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

# 結果を保存
cv2.imwrite("contours.png", img)
