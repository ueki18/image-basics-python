import cv2
import numpy as np

# 二値画像を読み込み（白が物体，黒が背景）
binary = cv2.imread("objects_clean.png", cv2.IMREAD_GRAYSCALE)

# ラベリングを実行
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary)

print(f"検出された物体数: {num_labels - 1}")  # 背景（ラベル0）を除く

# ラベル1以降が物体（ラベル0は背景のためスキップ）
for i in range(1, num_labels):
    # stats[i] から面積と外接矩形の情報を取得
    area   = stats[i, cv2.CC_STAT_AREA]
    x      = stats[i, cv2.CC_STAT_LEFT]    # 外接矩形の左上のX座標
    y      = stats[i, cv2.CC_STAT_TOP]     # 外接矩形の左上のY座標
    width  = stats[i, cv2.CC_STAT_WIDTH]   # 外接矩形の幅
    height = stats[i, cv2.CC_STAT_HEIGHT]  # 外接矩形の高さ

    # 重心座標
    cx, cy = centroids[i]

    print(f"物体{i:2d}: 面積={area:5d}, 重心=({cx:.1f}, {cy:.1f}), "
          f"外接矩形=({x}, {y}, {width}, {height})")
