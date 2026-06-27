import cv2

# グレースケールで読み込み
img = cv2.imread("objects.png", cv2.IMREAD_GRAYSCALE)

# しきい値を127に固定して二値化
# ret: 実際に使用されたしきい値（固定の場合は127がそのまま返る）
# binary: 二値化後の画像
ret, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

print(f"使用されたしきい値: {ret}")
cv2.imwrite("binary_127.png", binary)
