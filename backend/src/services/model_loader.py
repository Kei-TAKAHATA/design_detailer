import torch
# transformersのモデルを使用する場合
from transformers import AutoModelForCausalLM, AutoTokenizer
# llama_cppのモデルを使用する場合
from llama_cpp import Llama

print("=== モデルロード開始 ===")
model_id = None
model_path = "models/elyza/ELYZA-japanese-Llama-2-7b-fast-instruct-q4_K_M.gguf"

# model_id = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
# メモリ不足
# model_id = "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"
# model_id = "deepseek-ai/DeepSeek-R1-Distill-Llama-8B"
# model_id = "elyza/ELYZA-japanese-Llama-2-7b"
# model_id = "elyza/ELYZA-japanese-Llama-2-7b-fast-instruct"


# デバイス自動判定
if torch.backends.mps.is_available():
    device = "mps"
elif torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"
print(f"使用デバイス: {device}")

try:
    if model_id:
        # transformersのモデルを使用する場合
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            torch_dtype=torch.float16 if device != "cpu" else torch.float32,
            device_map=device,
            trust_remote_code=True,
        )
    elif model_path:
        # llama_cppのモデルを使用する場合
        tokenizer = None  # llama-cpp-pythonは独自のトークナイザーを内包
        model = Llama(model_path=model_path, n_ctx=2048, n_gpu_layers=32)
    else:
        raise ValueError("model_id または model_path を指定してください")
except Exception as e:
    print("モデルまたはトークナイザーのロードに失敗しました:", e)
    raise

print("=== モデルロード完了 ===")
