import cv2
import numpy as np

width, height = 640, 480
image = np.ones((height, width, 3), dtype=np.uint8) * 255

start_point = (0, height // 2)
end_point = (0, height // 2)
speed = 5  # 動かす速度

while True:
    # 前の線を消すために画像を再度白くする
    image[:] = 255

    cv2.line(image, start_point, end_point, (0, 0, 255), 5)

    # 終点を右に移動
    end_point = (end_point[0] + speed, end_point[1])

    cv2.imshow("Line Animation", image)

    if cv2.waitKey(30) == 27:  # Escキーが押されたら終了
        break
    if end_point[0] > width:  # 画面端に達したら終了
        break

cv2.destroyAllWindows()
