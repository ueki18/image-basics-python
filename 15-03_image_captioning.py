from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# BLIPモデル専用のプロセッサとモデルを読み込む
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# 画像を読み込んでキャプションを生成
image = Image.open("input.png").convert("RGB")
inputs = processor(image, return_tensors="pt")
out = model.generate(**inputs)

print(processor.decode(out[0], skip_special_tokens=True))
