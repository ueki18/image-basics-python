import cv2

cap = cv2.VideoCapture("sample_video.mp4")
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    fgmask = fgbg.apply(frame)

    # 輪郭を抽出
    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        # 面積が小さいノイズは無視する
        if cv2.contourArea(cnt) > 500:
            # 輪郭を囲む外接矩形を取得
            x, y, w, h = cv2.boundingRect(cnt)
            # 元のフレームに緑色の枠を描画
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # （オプション）重心を計算して赤い点を打つ
            M = cv2.moments(cnt)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)

    cv2.imshow("Tracking", frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
