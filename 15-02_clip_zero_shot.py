from transformers import pipeline

classifier = pipeline("zero-shot-image-classification", model="openai/clip-vit-base-patch32")

# あらかじめ学習していないクラス名でも分類できる
candidate_labels = ["a photo of a dog", "a photo of a cat", "a photo of a car"]
results = classifier("input.png", candidate_labels=candidate_labels)

for result in results:
    print(f"{result['label']}: {result['score']:.2f}")
