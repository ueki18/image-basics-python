import cv2

img = cv2.imread("low_contrast.png", cv2.IMREAD_GRAYSCALE)

# CLAHEオブジェクトの生成
# clipLimit: コントラストの制限値, tileGridSize: 分割するブロックのサイズ
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

# 適用
img_clahe = clahe.apply(img)

cv2.imwrite("clahe_output.png", img_clahe)
