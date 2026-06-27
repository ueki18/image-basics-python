import cv2
import numpy as np

noisy_img = cv2.imread("noisy_img.png", cv2.IMREAD_GRAYSCALE)
kernel = np.ones((3, 3), dtype=np.uint8)

# --- 開処理（収縮 → 膨張）：背景の白いノイズを除去 ---

# 方法1: erode と dilate を組み合わせる
opening_manual = cv2.dilate(
    cv2.erode(noisy_img, kernel, iterations=1),
    kernel, iterations=1
)

# 方法2: morphologyEx で一括実行（方法1と同じ結果）
opening = cv2.morphologyEx(noisy_img, cv2.MORPH_OPEN, kernel)

# --- 閉処理（膨張 → 収縮）：文字内部の黒い穴を埋める ---

# 開処理の結果に閉処理を重ねて適用する
clean_img = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

cv2.imwrite("opening.png",        opening)
cv2.imwrite("opening_manual.png", opening_manual)
cv2.imwrite("clean_img.png",  clean_img)
