import torch
# Transformers対応モデルを使用する場合
from transformers import AutoModelForCausalLM, AutoTokenizer
# llama_cpp対応モデルを使用する場合
from llama_cpp import Llama

print("=== モデルロード開始 ===")
model_id = None  # Transformers対応モデルを使用する場合に指定
model_path = None  # llama_cpp対応モデルを使用する場合に指定

model_name = "elyza"
model_path = "models/elyza/Llama-3-ELYZA-JP-8B-q4_k_m.gguf"

# 普通
# model_name = "rakuten"
# model_path = "models/rakuten/RakutenAI-7B-instruct-q3_K_M.gguf"

# 微妙
# model_name = "deepseek"
# model_path = "models/deepseek/DeepSeek-R1-Distill-Qwen-7B-Q4_K_M.gguf"

# model_name = "deepseek"
# model_id = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"

# 厳しい
# model_name = "plamo"
# model_path = "models/plamo/plamo-13b-Q4_K_M.gguf"

# 良い
# model_name = "elyza"
# model_path = "models/elyza/Llama-3-ELYZA-JP-8B-q4_k_m.gguf"
# model_path = "models/elyza/ELYZA-japanese-Llama-2-7b-fast-instruct-q4_K_M.gguf"

# model_name = "swallow_ms"
# model_path = "models/swallow_ms/tokyotech-llm-Swallow-MS-7b-instruct-v0.1-IQ4_NL.gguf"

# トークン数不足
# model_name = "cyberagent"
# model_path = "models/cyberagent/cyberagent-open-calm-7b-q4_K_M.gguf"

# メモリ不足
# llama_cpp対応モデル
# model_id = None
# model_name = "deepseek"
# model_path = "models/deepseek/deepseek-coder-6.7b-instruct.Q3_K_M.gguf"
# model_path = "models/deepseek/deepseek-coder-6.7b-instruct.Q3_K_L.gguf"
# model_path = "models/deepseek/deepseek-coder-6.7b-instruct.Q4_K_S.gguf"

# model_name = "cyberagent"
# model_path = "models/cyberagent/cyberagent-calm2-7b-chat-dpo-experimental-q4_K_M.gguf"

# Transformers対応モデル
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
        # Transformers対応モデルを使用する場合
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            torch_dtype=torch.float16 if device != "cpu" else torch.float32,
            device_map=device,
            trust_remote_code=True,
        )
        max_ctx = tokenizer.model_max_length
        # context_windowが大きすぎるとメモリーオーバーになるので4096に制限
        context_window = min(max_ctx, 4096)
        print(f"max_ctx: {max_ctx}")
        print(f"context_window: {context_window}")
    elif model_path:
        # llama_cpp対応モデルを使用する場合
        tokenizer = None  # llama-cpp-pythonは独自のトークナイザーを内包

        # modelごとにcontext_windowが異なるため、最大値を取得し利用する。
        # 一度読み込んでから出ないと最大値を取得できないので、
        # 1.仮読み込み、2.context_windowの最大値取得、3.破棄、4.context_windowの最大値で再度読み込み
        # の流れで対応する。

        # 1. 仮の小さいn_ctxで一度ロード
        tmp_model = Llama(model_path=model_path, n_ctx=512)
        # 2. 最大値を取得（バージョンによって属性名が違う場合あり）
        # 属性がn_ctx_trainの場合、n_ctxの場合、どちらもない場合があるので、全ての場合に対応できるようにする。
        max_ctx = int(tmp_model.metadata.get("llama.context_length", 2048))
        # 3. メモリ節約のため破棄
        del tmp_model

        # 4. 最大値で再度ロード
        model = Llama(model_path=model_path, n_ctx=max_ctx, n_gpu_layers=32)
        # context_windowが大きすぎるとメモリーオーバーになるので4096に制限
        context_window = min(max_ctx, 4096)
        print(f"max_ctx: {max_ctx}")
        print(f"context_window: {context_window}")
    else:
        raise ValueError("model_id または model_path を指定してください")
except Exception as e:
    print("モデルまたはトークナイザーのロードに失敗しました:", e)
    raise

print("=== モデルロード完了 ===")
