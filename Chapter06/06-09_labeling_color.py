import cv2
import numpy as np

binary = cv2.imread("objects_clean.png", cv2.IMREAD_GRAYSCALE)
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary)

# 各ラベルにランダムな色を割り当てる（ラベル0の背景は黒のまま）
colors = np.zeros((num_labels, 3), dtype=np.uint8)
colors[1:] = np.random.randint(50, 255, size=(num_labels - 1, 3))

# labels 配列の各画素をカラーに変換
colored = colors[labels]

cv2.imwrite("objects_labeled.png", colored)
