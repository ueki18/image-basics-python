import cv2

cap = cv2.VideoCapture(0)

# フレームサイズを取得（VideoWriterに渡すため）
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# コーデック（FourCC）の指定．mp4形式なら'mp4v'を用いることが多い
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# 出力ファイル名，コーデック，fps，フレームサイズを指定して書き出し用オブジェクトを作成
writer = cv2.VideoWriter("output.mp4", fourcc, 30.0, (width, height))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 読み込んだフレームを1枚ずつファイルに書き込む
    writer.write(frame)

    cv2.imshow("Recording", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()
