import cv2

# Webカメラを開く（0番目のカメラデバイスを指定）
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("カメラを開けませんでした")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("フレームを取得できませんでした")
        break

    cv2.imshow("Webcam", frame)

    # 1ミリ秒待機．'q'キーが押されたら終了する
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
