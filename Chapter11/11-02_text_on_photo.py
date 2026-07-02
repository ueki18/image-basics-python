import cv2

# 画像の読み込み
image = cv2.imread("panda.png")

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (0, 0, 255)  # 赤色
thickness = 2
text = "Hello, OpenCV!"

text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
text_x = (image.shape[1] - text_size[0]) // 2
text_y = (image.shape[0] + text_size[1]) // 2

cv2.putText(image, text, (text_x, text_y), font, font_scale, font_color, thickness)

cv2.imshow("Image with Text", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
