import cv2
img = cv2.imread("sample.jpg")
print(type(img))    # <class 'numpy.ndarray'>
print(img.shape)    # (高さ, 幅, チャンネル数) 例: (480, 640, 3)
print(img.dtype)    # uint8
print(img.size)     # 総要素数 例: 921600
