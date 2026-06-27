import cv2

img = cv2.imread("newspaper.png", cv2.IMREAD_GRAYSCALE)

# 大津の方法を適用
# しきい値の引数（0）は無視され，自動計算された値が ret に返る
ret, otsu_binary = cv2.threshold(
    img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

print(f"自動決定されたしきい値: {ret}")
cv2.imwrite("otsu.png", otsu_binary)
