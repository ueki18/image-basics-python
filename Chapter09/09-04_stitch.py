import cv2
img1 = cv2.imread("left.png")
img2 = cv2.imread("right.png")
stitcher = cv2.Stitcher_create()
status, pano = stitcher.stitch([img1, img2])
if status == cv2.Stitcher_OK:
    cv2.imwrite("stitch_result.png", pano)
    print("パノラマ合成成功")
else:
    print(f"合成エラー（エラーコード：{status}）")
