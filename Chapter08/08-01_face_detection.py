import cv2

# OpenCVに同梱されている学習済みカスケード分類器を読み込む
cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

img = cv2.imread("people.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 顔検出の実行
# scaleFactor: 画像を縮小する割合, minNeighbors: 検出の信頼性に関わるパラメータ
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

print(f"検出された顔の数: {len(faces)}")

# 検出した顔の周りに矩形を描画
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imwrite("face_detection.png", img)
