from PIL import Image
img = Image.open("sample.jpg")  # 画像の読み込み
img.show()                      # 既定のビューアで表示
print(img.size)                 # 画像サイズ (幅, 高さ) を確認
print(img.mode)                 # 色モード（例: RGB, L）を確認
