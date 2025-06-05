import time

from transformers import PreTrainedTokenizerBase, PreTrainedModel
from llama_cpp import Llama

from config.config_loader import PROMPT_TEMPLATES
from .model_loader import tokenizer, model, model_name, context_window


def select_mermaid_prompt(
    design_detail: str,
    model_: PreTrainedModel | Llama,
    tokenizer_: PreTrainedTokenizerBase | None,
    context_window_: int,
    mermaid_prompt_template: str,
    max_tokens: int = 500,
) -> str:
    """
    設計詳細テキストをMermaid記法の図に変換するためのプロンプトを選択する。

    Parameters
    ----------
    design_detail : str
        設計詳細のテキスト
    model_ : PreTrainedModel | Llama
        トークナイズや推論に使用するモデルインスタンス
    tokenizer_ : PreTrainedTokenizerBase | None
        トークナイズに使用するトークナイザー
    context_window_ : int
        モデルのコンテキストウィンドウサイズ
    mermaid_prompt_template : str
        プロンプトテンプレート
    max_tokens : int, default 500
        生成時に確保する最大トークン数

    Returns
    -------
    str
        選択されたプロンプト文字列
    """
    detailed_prompt = mermaid_prompt_template["detailed"]["template"].format(design_detail=design_detail)
    simple_prompt = mermaid_prompt_template["simple"]["template"].format(design_detail=design_detail)
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


def convert_design_detail_to_mermaid(design_detail: str) -> str:
    """
    設計詳細テキストをMermaid記法の図に変換する。

    Parameters
    ----------
    design_detail : str
        設計詳細のテキスト
    count : int, optional
        追加のオプション。2の場合は別パターンを返す。

    Returns
    -------
    str
        Mermaid記法のシーケンス図
    """
    if model_name in PROMPT_TEMPLATES["mermaid"]:
        mermaid_prompt_template = PROMPT_TEMPLATES["mermaid"][model_name]
    else:
        print("モデル未指定時のMermaid生成用プロンプトを使用します")
        mermaid_prompt_template = PROMPT_TEMPLATES["mermaid"]["default"]

    # mermaid_prompt_template = PROMPT_TEMPLATES["mermaid"][model_name]
    max_tokens = 500
    prompt = select_mermaid_prompt(
        design_detail=design_detail,
        model_=model,
        tokenizer_=tokenizer,
        context_window_=context_window,
        mermaid_prompt_template=mermaid_prompt_template,
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
        mermaid = tokenizer.decode(outputs[0][input_length:], skip_special_tokens=True)
        print(f"デコード完了: {time.time() - start:.2f}秒")
    else:
        # llama_cpp対応モデルを使用する場合
        outputs = model(prompt, max_tokens=max_tokens)
        print(f"モデル推論完了: {time.time() - start:.2f}秒")
        mermaid = outputs["choices"][0]["text"]
    return mermaid
