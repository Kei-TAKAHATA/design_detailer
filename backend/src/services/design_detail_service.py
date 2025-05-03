import time

from .model_loader import tokenizer, model


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
    # 設計の概要をモデルに入力
    prompt = (
        "あなたはシステム設計の専門家です。\n"
        "以下の設計概要をもとに、設計詳細を日本語で3つ以上の箇条書きで出力してください。\n"
        "例:\n"
        "【設計概要】\n"
        "人（ユーザー）が設計の概要を書いたら、大きな流れ、図を作成した結果を自動生成するツールを作成する。\n"
        "【設計詳細】\n"
        "1. ユーザーインターフェース (React + TypeScript)\n"
        "   入力コンポーネント: 設計の概要を入力するためのテキストエリア。\n"
        "   出力コンポーネント: 変換されたMermaidフォーマットを表示するエリア。\n"
        "   変換されたMermaidフォーマットを表示するエリア。\n"
        "   生成された図を表示するエリア。\n"
        "   設計の概要と図をまとめて表示するエリア。\n"
        "   ボタンコンポーネント:\n"
        "       「変換」ボタン: 設計の概要をMermaidフォーマットに変換し、図を生成する。\n"
        "       「出力」ボタン: 設計の概要と生成された図をまとめて表示する。\n"
        "2. バックエンドロジック\n"
        "   入力解析: ユーザーの入力を解析し、Mermaidフォーマットに変換するロジックを実装。\n"
        "   GPTのAPIを使用して自然言語を解析し、適切なMermaidコードを生成。\n"
        "3. フロントエンドロジック (React + TypeScript)\n"
        "   Mermaidの統合: Mermaid.jsを使用して、Mermaidフォーマットから図を生成。\n"
        "   生成された図をユーザーインターフェースに表示。\n"
        "   出力の統合: 設計の概要と生成された図をまとめて表示するためのロジックを実装。\n"
        "【設計概要】\n"
        f"{design_summary}\n"
        "【設計詳細】"
    )
    start = time.time()
    print("=== 推論開始 ===")
    # prompt = "Think in English and response in Japanese:\n: テストと返して！"
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    print(f"トークナイズ完了: {time.time() - start:.2f}秒")
    outputs = model.generate(**inputs, max_new_tokens=1000)
    print(f"モデル推論完了: {time.time() - start:.2f}秒")
    input_length = inputs['input_ids'].shape[1]
    design_detail = tokenizer.decode(outputs[0][input_length:], skip_special_tokens=True)
    print(f"デコード完了: {time.time() - start:.2f}秒")

    # design_detail = """1. ユーザーインターフェース (React + TypeScript)
    #   入力コンポーネント:
    #   設計の概要を入力するためのテキストエリア。
    #   出力コンポーネント:
    #   変換されたMermaidフォーマットを表示するエリア。
    #   Mermaid.jsを使用して生成された図を表示するエリア。
    #   設計の概要と図をまとめて表示するエリア。
    #   ボタンコンポーネント:
    #   「変換」ボタン: 設計の概要をMermaidフォーマットに変換し、図を生成する。
    #   「出力」ボタン: 設計の概要と生成された図をまとめて表示する。
    #   2. バックエンドロジック
    #   入力解析:
    #   ユーザーの入力を解析し、Mermaidフォーマットに変換するロジックを実装。
    #   GPTのAPIを使用して自然言語を解析し、適切なMermaidコードを生成。
    #   3. フロントエンドロジック (React + TypeScript)
    #   Mermaidの統合:
    #   Mermaid.jsを使用して、Mermaidフォーマットから図を生成。
    #   生成された図をユーザーインターフェースに表示。
    #   出力の統合:
    #   設計の概要と生成された図をまとめて表示するためのロジックを実装。"""
    return design_detail
