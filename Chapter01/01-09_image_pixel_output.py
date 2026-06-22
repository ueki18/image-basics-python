import cv2
img = cv2.imread("sample.jpg", cv2.IMREAD_GRAYSCALE)  # グレースケールで読み込む
height, width = img.shape
f_out = open("pixel_values.txt", "w")
for y in range(height):
    for x in range(width):
        f_out.write("%4d " % img[y, x])
    f_out.write("\n")
f_out.close()
