from PIL import Image
img = Image.open("sample.jpg")   # 画像の読み込み
img.save("output.png")           # PNG形式で保存
