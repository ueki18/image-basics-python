import cv2
import numpy as np

binary = cv2.imread("objects_clean.png", cv2.IMREAD_GRAYSCALE)
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary)

# 面積がこの値以下の連結成分はノイズとみなして無視する
min_area = 500

# 面積フィルタリング後の物体数をカウント
object_count = 0
for i in range(1, num_labels):
    area = stats[i, cv2.CC_STAT_AREA]
    if area >= min_area:
        object_count += 1

print(f"有効な物体数: {object_count}")
