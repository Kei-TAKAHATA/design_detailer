import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

print("=== モデルロード開始 ===")
model_id = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
# メモリ不足
# model_id = "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"
# model_id = "deepseek-ai/DeepSeek-R1-Distill-Llama-8B"

# デバイス自動判定
if torch.backends.mps.is_available():
    device = "mps"
elif torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"
print(f"使用デバイス: {device}")

try:
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype=torch.float16 if device != "cpu" else torch.float32,
        device_map=device,
        trust_remote_code=True,
    )
except Exception as e:
    print("モデルまたはトークナイザーのロードに失敗しました:", e)
    raise

print("=== モデルロード完了 ===")
