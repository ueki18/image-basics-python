import torch
from diffusers import StableDiffusionUpscalePipeline
from PIL import Image

pipe = StableDiffusionUpscalePipeline.from_pretrained(
    "stabilityai/stable-diffusion-x4-upscaler",
    torch_dtype=torch.float16,
)
pipe = pipe.to("cuda")

low_res_image = Image.open("low_res.png").convert("RGB")
upscaled_image = pipe(prompt="", image=low_res_image).images[0]

upscaled_image.save("upscaled.png")
