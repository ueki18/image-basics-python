import cv2
img = cv2.imread("sample.jpg")  # 画像をNumPy配列として読み込む
print(img.shape)                # 配列の形状 (高さ, 幅, チャンネル数)
cv2.imshow("image", img)        # ウィンドウに表示
cv2.waitKey(0)                  # キー入力を待つ
cv2.destroyAllWindows()         # ウィンドウを閉じる
