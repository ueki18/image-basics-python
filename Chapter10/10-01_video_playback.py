import cv2

# 動画ファイルを開く
cap = cv2.VideoCapture("sample_video.mp4")

# 動画が正しく開けたか確認
if not cap.isOpened():
    print("動画を開けませんでした")
    exit()

# ループで1フレームずつ読み込んで表示する
while True:
    # ret: 読み込み成功かどうかのフラグ(True/False)
    # frame: 読み込んだ1枚の画像（NumPy配列）
    ret, frame = cap.read()

    # 動画の最後まで到達して読み込めなくなったらループを抜ける
    if not ret:
        print("再生終了")
        break

    cv2.imshow("Video Playback", frame)

    # 30ミリ秒待機．キーボードの'q'キーが押されたら中断する
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# リソースを解放し，ウィンドウを閉じる
cap.release()
cv2.destroyAllWindows()
