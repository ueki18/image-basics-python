import cv2
img = cv2.imread("sample.jpg")   # 画像の読み込み
cv2.imwrite("output.jpg", img)   # output.jpg として保存
