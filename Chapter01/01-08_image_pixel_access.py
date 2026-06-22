import cv2

img = cv2.imread("sample.jpg")

# 1画素の値を取得（カラー画像の場合，BGR順）
print(img[100, 200])

# 特定チャンネルの値を取得
b = img[100, 200, 0]
g = img[100, 200, 1]
r = img[100, 200, 2]

# 画素値を白に変更
img[100, 200] = [255, 255, 255]

# 変更後の値を確認
print(img[100, 200])
