import torch
from diffusers import StableDiffusionPipeline

# 学習済みのStable Diffusionモデルを読み込む
pipe = StableDiffusionPipeline.from_pretrained(
    "stable-diffusion-v1-5/stable-diffusion-v1-5",
    torch_dtype=torch.float16,
)
pipe = pipe.to("cuda")

# プロンプト（テキスト指示）から画像を生成
prompt = "a futuristic city in cyberpunk style"
image = pipe(prompt).images[0]

# 生成した画像を保存
image.save("generated.png")
