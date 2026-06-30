import cv2

cap = cv2.VideoCapture("sample_video.mp4")
ret, prev_frame = cap.read()
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

while True:
    ret, current_frame = cap.read()
    if not ret:
        break

    current_gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)

    # 1. 前フレームと現在のフレームの差分（絶対値）を計算
    diff = cv2.absdiff(prev_gray, current_gray)

    # 2. しきい値処理で二値化し，変化があったピクセルを真っ白(255)にする
    _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    cv2.imshow("Difference", thresh)

    # 次のループのために，現在のフレームを「前フレーム」として保存
    prev_gray = current_gray

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
