import cv2
img = cv2.imread("landscape.png")
# BGRからグレースケールへ変換
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray_output.png", gray)
