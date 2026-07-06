import torch
from diffusers import StableDiffusionInpaintPipeline
from PIL import Image

pipe = StableDiffusionInpaintPipeline.from_pretrained(
    "stable-diffusion-v1-5/stable-diffusion-inpainting",
    torch_dtype=torch.float16,
)
pipe = pipe.to("cuda")

# 元画像と，再描画する範囲（白）を示したマスク画像を読み込む
init_image = Image.open("input.png").convert("RGB")
mask_image = Image.open("mask.png").convert("RGB")

prompt = "a cat sitting on the grass"
image = pipe(prompt=prompt, image=init_image, mask_image=mask_image).images[0]

image.save("inpaint_result.png")
