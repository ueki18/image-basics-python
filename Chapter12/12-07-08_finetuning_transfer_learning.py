import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.models as models
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from PIL import Image

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


# --- 評価用関数（「学習ループと評価」の節で定義したものと同じ） ---
def evaluate(model, data_loader):
    """指定したデータに対する正解率(Accuracy)を計算する"""
    model.eval()
    correct, total = 0, 0
    with torch.no_grad():
        for images, labels in data_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    return correct / total


# ImageNetの事前学習済みモデルに合わせた前処理
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                          std=[0.229, 0.224, 0.225]),
])

# data/train/クラス名/*.jpg のようなフォルダ構成から読み込む
train_dataset = datasets.ImageFolder('data/train', transform=transform)
val_dataset   = datasets.ImageFolder('data/val', transform=transform)
train_loader  = DataLoader(train_dataset, batch_size=16, shuffle=True)
val_loader    = DataLoader(val_dataset, batch_size=16, shuffle=False)

print('クラス一覧:', train_dataset.classes)  # フォルダ名がそのままクラス名になる

# ImageNetで事前学習済みのResNet-18を読み込む
finetune_model = models.resnet18(pretrained=True)

# 畳み込み層のパラメータを固定し，学習されないようにする
for param in finetune_model.parameters():
    param.requires_grad = False

# 最後の全結合層だけを，フォルダから読み込んだクラス数に合わせて付け替える
num_classes = len(train_dataset.classes)
finetune_model.fc = nn.Linear(finetune_model.fc.in_features, num_classes)
finetune_model = finetune_model.to(device)

criterion = nn.CrossEntropyLoss()
# 学習対象は付け替えた全結合層のパラメータのみ
optimizer = optim.Adam(finetune_model.fc.parameters(), lr=0.001)

num_epochs = 5
for epoch in range(num_epochs):
    finetune_model.train()
    running_loss = 0.0
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = finetune_model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()

    train_acc = evaluate(finetune_model, train_loader)
    val_acc = evaluate(finetune_model, val_loader)
    print(f'Epoch {epoch+1}/{num_epochs}  Loss: {running_loss/len(train_loader):.3f}  '
          f'Train Acc: {train_acc:.3f}  Val Acc: {val_acc:.3f}')


# --- ファインチューニングしたモデルで新しい画像を分類する ---
def predict_image(model, image_path, class_names):
    image = Image.open(image_path).convert('RGB')
    input_tensor = transform(image).unsqueeze(0).to(device)
    model.eval()
    with torch.no_grad():
        outputs = model(input_tensor)
        probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
    top_prob, top_idx = torch.max(probabilities, dim=0)
    return class_names[top_idx], top_prob.item()


predicted_class, prob = predict_image(finetune_model, 'new_photo.jpg', train_dataset.classes)
print(f'{predicted_class} ({prob*100:.1f}%)')
