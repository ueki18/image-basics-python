from PIL import Image
from transformers import Qwen2VLForConditionalGeneration, AutoProcessor

# Qwen2-VLの軽量版（2Bパラメータ）を読み込む
model = Qwen2VLForConditionalGeneration.from_pretrained(
    "Qwen/Qwen2-VL-2B-Instruct", torch_dtype="auto", device_map="auto"
)
processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-2B-Instruct")

# 画像と質問文をチャット形式で用意する
image = Image.open("input.png").convert("RGB")
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image"},
            {"type": "text", "text": "What animal is in this picture?"},
        ],
    }
]

# チャットテンプレートに沿ってテキストを整形し，画像と一緒にモデルへ入力
text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = processor(text=[text], images=[image], return_tensors="pt").to(model.device)

# 回答を生成する
generated_ids = model.generate(**inputs, max_new_tokens=64)
generated_ids_trimmed = generated_ids[:, inputs.input_ids.shape[1]:]
output_text = processor.batch_decode(generated_ids_trimmed, skip_special_tokens=True)

print(output_text[0])
