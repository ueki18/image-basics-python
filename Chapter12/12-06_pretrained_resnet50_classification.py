import torch
from torchvision import models, transforms
from PIL import Image
import json
import urllib.request

# ImageNetで事前学習済みのResNet-50を読み込み，推論モードにする
model = models.resnet50(pretrained=True)
model.eval()

# 学習時と同じ前処理（サイズ変更・正規化）を行う
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                          std=[0.229, 0.224, 0.225]),
])

image = Image.open('sample.jpg').convert('RGB')
input_tensor = preprocess(image).unsqueeze(0)  # バッチ次元を追加

with torch.no_grad():
    outputs = model(input_tensor)
    probabilities = torch.nn.functional.softmax(outputs[0], dim=0)

# ImageNetの1000クラスのラベル名を取得
url = ('https://raw.githubusercontent.com/anishathalye/'
       'imagenet-simple-labels/master/imagenet-simple-labels.json')
labels = json.load(urllib.request.urlopen(url))

# 確率が高い上位5クラスを表示
top5_prob, top5_idx = torch.topk(probabilities, 5)
for prob, idx in zip(top5_prob, top5_idx):
    print(f'{labels[idx]}: {prob.item()*100:.2f}%')
