from PIL import Image
img = Image.open("sample.jpg")   # 画像の読み込み
img.save("output.jpg", quality=80)
