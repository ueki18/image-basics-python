import cv2
import numpy as np

# 人物（グリーンバック）と背景画像の読み込み
person = cv2.imread("person_green.png")
background = cv2.imread("background.png")

# 背景を人物画像と同じサイズにリサイズ
background = cv2.resize(background, (person.shape[1], person.shape[0]))

# HSV色空間に変換して緑色のマスクを作成
hsv = cv2.cvtColor(person, cv2.COLOR_BGR2HSV)
lower_green = np.array([40, 50, 50])
upper_green = np.array([80, 255, 255])
mask_green = cv2.inRange(hsv, lower_green, upper_green)

# マスクを反転（人物部分が白，背景部分が黒）
mask_person = cv2.bitwise_not(mask_green)

# 人物部分と背景部分をそれぞれ切り出して合成
person_part = cv2.bitwise_and(person, person, mask=mask_person)
background_part = cv2.bitwise_and(background, background, mask=mask_green)
result = cv2.add(person_part, background_part)

cv2.imwrite("composited.jpg", result)
