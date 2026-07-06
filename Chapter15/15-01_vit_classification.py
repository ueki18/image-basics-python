from transformers import pipeline

# ViTモデルを用いた画像分類パイプラインを作成
classifier = pipeline("image-classification", model="google/vit-base-patch16-224")

results = classifier("input.png")

# 確信度が高い上位3件を表示
for result in results[:3]:
    print(f"{result['label']}: {result['score']:.2f}")
