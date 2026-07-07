import cv2
import matplotlib.pyplot as plt

# グレースケールで画像を読み込む
img_gray = cv2.imread("low_contrast.png", cv2.IMREAD_GRAYSCALE)

# ヒストグラムの計算
# 引数: [画像], [チャンネル], マスク, [ビン数], [範囲]
hist = cv2.calcHist([img_gray], [0], None, [256], [0, 256])

# グラフの描画
plt.plot(hist, color='black')
plt.title('Grayscale Histogram')
plt.xlabel('Pixel Value (0-255)')
plt.ylabel('Frequency')
plt.xlim([0, 256])
plt.grid(True, alpha=0.5)
plt.show()
