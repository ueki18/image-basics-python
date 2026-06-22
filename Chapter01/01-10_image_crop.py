import cv2
img = cv2.imread("sample.jpg")

# img[上端:下端, 左端:右端]
crop = img[100:200, 100:300]    # 縦100px・横200pxの領域を切り出す
cv2.imwrite("crop.png", crop)   # 切り出した画像を保存

# スライシングで範囲を指定して画素値を一括変更することもできる
img[100:200, 100:300] = [0, 0, 0]   # 同じ領域を黒に塗りつぶす
cv2.imwrite("painted.png", img)     # 塗りつぶした画像を保存
