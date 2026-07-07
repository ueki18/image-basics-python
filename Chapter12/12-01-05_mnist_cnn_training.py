import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader, random_split
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix


# --- モデルの定義 ---
class SimpleCNN(nn.Module):
    def __init__(self, num_classes=10):
        super(SimpleCNN, self).__init__()
        # 1つ目の畳み込み層 (入力チャネル1(グレースケール), 出力32, カーネル3x3)
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, padding=1)
        # 2つ目の畳み込み層
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        # 最大プーリング層 (2x2)
        self.pool = nn.MaxPool2d(2, 2)
        # 全結合層 (28x28の画像がプーリングを2回経て7x7になることに注意)
        self.fc1 = nn.Linear(64 * 7 * 7, 512)
        self.fc2 = nn.Linear(512, num_classes)

    def forward(self, x):
        # 畳み込み -> ReLU -> プーリング の順でデータを流す
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        # 2次元の画像を1次元のベクトルに平坦化(Flatten)
        x = x.view(-1, 64 * 7 * 7)
        # 全結合層
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x


# --- データの準備 ---
# 画像をTensorに変換し，画素値を[-1, 1]の範囲に正規化
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,)),
])

# MNISTデータセットのダウンロード（初回のみ）
full_train_dataset = datasets.MNIST(
    root='./data', train=True, download=True, transform=transform)
test_dataset = datasets.MNIST(
    root='./data', train=False, download=True, transform=transform)

# 学習データ(60,000枚)を，学習用(train)と検証用(val)に分割する
# 検証データは学習中の様子見（ハイパーパラメータ調整の判断材料）に使い，
# テストデータ(test_dataset)は学習が全て終わった後の最終評価にのみ使う
val_size = 6000
train_size = len(full_train_dataset) - val_size
train_subset, val_subset = random_split(
    full_train_dataset, [train_size, val_size])

# ミニバッチ単位でデータを取り出すためのDataLoader
train_loader = DataLoader(train_subset, batch_size=64, shuffle=True)
val_loader   = DataLoader(val_subset, batch_size=64, shuffle=False)
test_loader  = DataLoader(test_dataset, batch_size=64, shuffle=False)


# --- モデル・損失関数・optimizerの準備 ---
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = SimpleCNN(num_classes=10).to(device)

# 多クラス分類なので交差エントロピー誤差を使用
criterion = nn.CrossEntropyLoss()
# Adamは学習率の調整が比較的簡単で扱いやすいoptimizer
optimizer = optim.Adam(model.parameters(), lr=0.001)


# --- 評価用関数の定義 ---
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


# --- 学習ループ ---
num_epochs = 5  # MNISTは比較的簡単なタスクなので少ないエポックでも精度が上がる
for epoch in range(num_epochs):
    model.train()
    running_loss = 0.0
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)

        optimizer.zero_grad()          # 勾配を初期化
        outputs = model(images)        # 順伝播（予測）
        loss = criterion(outputs, labels)
        loss.backward()                # 逆伝播（勾配の計算）
        optimizer.step()               # パラメータの更新

        running_loss += loss.item()

    train_acc = evaluate(model, train_loader)
    val_acc = evaluate(model, val_loader)
    print(f'Epoch {epoch+1}/{num_epochs}  Loss: {running_loss/len(train_loader):.3f}  '
          f'Train Acc: {train_acc:.3f}  Val Acc: {val_acc:.3f}')


# --- テストデータでの最終評価 ---
test_acc = evaluate(model, test_loader)
print(f'Test Acc: {test_acc:.3f}')

# --- モデルの保存 ---
torch.save(model.state_dict(), 'simple_cnn_mnist.pth')
# 保存したモデルを読み込む場合は以下のようにする
# model = SimpleCNN(num_classes=10).to(device)
# model.load_state_dict(torch.load('simple_cnn_mnist.pth'))

# --- 予測結果の可視化（テスト画像10枚を表示） ---
model.eval()
images, labels = next(iter(test_loader))
images, labels = images.to(device), labels.to(device)
with torch.no_grad():
    outputs = model(images)
    _, predicted = torch.max(outputs, 1)

fig, axes = plt.subplots(2, 5, figsize=(10, 4))
for i, ax in enumerate(axes.flat):
    img = images[i].cpu().squeeze(0) * 0.5 + 0.5  # 正規化を元の画素値に戻す
    ax.imshow(img, cmap='gray')
    color = 'blue' if predicted[i] == labels[i] else 'red'
    ax.set_title(f'pred:{predicted[i].item()} true:{labels[i].item()}', color=color, fontsize=9)
    ax.axis('off')
plt.tight_layout()
plt.savefig('prediction_samples.png')

# --- 混同行列の表示 ---
all_preds, all_labels = [], []
with torch.no_grad():
    for images, labels in test_loader:
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        _, predicted = torch.max(outputs, 1)
        all_preds.extend(predicted.cpu().numpy())
        all_labels.extend(labels.cpu().numpy())

cm = confusion_matrix(all_labels, all_preds, labels=list(range(10)))

fig, ax = plt.subplots(figsize=(6, 6))
im = ax.imshow(cm, cmap='Blues')
ax.set_xticks(range(10))
ax.set_yticks(range(10))
ax.set_xlabel('Predicted class')
ax.set_ylabel('True class')
ax.set_title('Confusion Matrix')
for i in range(10):
    for j in range(10):
        ax.text(j, i, cm[i, j], ha='center', va='center',
                 color='white' if cm[i, j] > cm.max() / 2 else 'black')
plt.colorbar(im)
plt.tight_layout()
plt.savefig('confusion_matrix.png')
