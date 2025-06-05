import time

from transformers import PreTrainedTokenizerBase, PreTrainedModel
from llama_cpp import Llama

from config.config_loader import PROMPT_TEMPLATES
from .model_loader import tokenizer, model, model_name, context_window


def select_design_detail_prompt(
    design_summary: str,
    model_: PreTrainedModel | Llama,
    tokenizer_: PreTrainedTokenizerBase | None,
    context_window_: int,
    design_detail_prompt_template: dict,
    max_tokens: int = 1000,
) -> str:
    """
    設計概要と各種パラメータに基づき、適切な設計詳細生成用プロンプトを選択する。

    Parameters
    ----------
    design_summary : str
        設計の概要テキスト。
    model_ : PreTrainedModel | Llama
        トークナイズや推論に使用するモデルインスタンス。
    tokenizer_ : PreTrainedTokenizerBase | None
        トークナイズに使用するトークナイザー。llama-cppの場合はNone。
    context_window_ : int
        モデルのコンテキストウィンドウサイズ。
    design_detail_prompt_template : dict
        detailed, simple などのテンプレートを含むプロンプトテンプレート辞書。
    max_tokens : int, default 1000
        生成時に確保する最大トークン数。

    Returns
    -------
    str
        選択されたプロンプト文字列。
    """
    detailed_prompt = design_detail_prompt_template["detailed"]["template"].format(design_summary=design_summary)
    simple_prompt = design_detail_prompt_template["simple"]["template"].format(design_summary=design_summary)
    # minimal_prompt = design_detail_prompt_template["minimal"].format(design_summary=design_summary)

    if tokenizer_:
        # Transformers対応モデルの場合
        detailed_tokens = tokenizer_.encode(detailed_prompt)
        print(f"detailed_tokens: {len(detailed_tokens)}")
        simple_tokens = tokenizer_.encode(simple_prompt)
        print(f"simple_tokens: {len(simple_tokens)}")
    else:
        # llama_cpp対応モデルの場合
        detailed_tokens = model_.tokenize(detailed_prompt.encode("utf-8"))
        print(f"detailed_tokens: {len(detailed_tokens)}")
        simple_tokens = model_.tokenize(simple_prompt.encode("utf-8"))
        print(f"simple_tokens: {len(simple_tokens)}")

    # detailed_promptとmax_tokensの合計がcontext_window_を超える場合はsimple_promptを使用
    if len(detailed_tokens) + max_tokens < context_window_:
        print("detailed_promptを使用します")
        return detailed_prompt
    print("simple_promptを使用します")
    return simple_prompt
    # elif len(simple_tokens) < context_window * 0.9:
    #     return simple_prompt
    # else:
    #     return minimal_prompt


def generate_design_detail(design_summary: str) -> str:
    """
    設計概要テキストから設計詳細テキストを生成する。

    Parameters
    ----------
    design_summary : str
        設計の概要テキスト。

    Returns
    -------
    str
        生成された設計詳細テキスト。
    """
    if model_name in PROMPT_TEMPLATES["design_detail"]:
        design_detail_prompt_template = PROMPT_TEMPLATES["design_detail"][model_name]
    else:
        print("モデル未指定時の設計詳細生成用プロンプトを使用します")
        design_detail_prompt_template = PROMPT_TEMPLATES["design_detail"]["default"]

    # design_detail_prompt_template = PROMPT_TEMPLATES["design_detail"][model_name]
    max_tokens = 1000
    prompt = select_design_detail_prompt(
        design_summary=design_summary,
        model_=model,
        tokenizer_=tokenizer,
        context_window_=context_window,
        design_detail_prompt_template=design_detail_prompt_template,
        max_tokens=max_tokens,
    )
    start = time.time()
    print("=== 推論開始 ===")
    if tokenizer:
        # Transformers対応モデルを使用する場合
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
        print(f"トークナイズ完了: {time.time() - start:.2f}秒")
        outputs = model.generate(**inputs, max_new_tokens=max_tokens)
        print(f"モデル推論完了: {time.time() - start:.2f}秒")
        input_length = inputs['input_ids'].shape[1]
        design_detail = tokenizer.decode(outputs[0][input_length:], skip_special_tokens=True)
        print(f"デコード完了: {time.time() - start:.2f}秒")
    else:
        # llama_cpp対応モデルを使用する場合
        outputs = model(prompt, max_tokens=max_tokens)
        print(f"モデル推論完了: {time.time() - start:.2f}秒")
        design_detail = outputs["choices"][0]["text"]
    return design_detail
