import cv2
import numpy as np

# 画像のサイズ
width, height = 640, 480

# 白い背景の画像を作成
image = np.ones((height, width, 3), dtype=np.uint8) * 255

# フォントの設定
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (0, 0, 0)  # 黒色
thickness = 2

# 文字を描く位置（画像の中央に配置）
text = "Hello, OpenCV!"
text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
text_x = (image.shape[1] - text_size[0]) // 2
text_y = (image.shape[0] + text_size[1]) // 2

# 文字を描画
cv2.putText(image, text, (text_x, text_y), font, font_scale, font_color, thickness)

cv2.imshow("Image with Text", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
