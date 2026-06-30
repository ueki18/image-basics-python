import cv2

cap = cv2.VideoCapture("sample_video.mp4")

# 背景差分アルゴリズムの初期化
# history: 背景モデルの学習に用いる過去フレーム数
# varThreshold: 前景とみなすためのマハラノビス距離のしきい値
# detectShadows: 影を検出するかどうか（グレーで出力される）
fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=True)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 背景モデルの更新と前景マスクの取得
    fgmask = fgbg.apply(frame)

    # （オプション）モルフォロジー演算でノイズを除去する
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    cv2.imshow("Foreground Mask", fgmask)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
