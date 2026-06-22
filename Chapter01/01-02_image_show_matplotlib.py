import cv2
import matplotlib.pyplot as plt
img = cv2.imread("sample.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # BGR -> RGB に変換
plt.imshow(img)
plt.axis("off")   # 軸（目盛り）を非表示にする
plt.show()
