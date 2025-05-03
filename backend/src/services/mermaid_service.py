import time

from .model_loader import tokenizer, model


def convert_design_detail_to_mermaid(design_detail: str, count: int | None = None) -> str:
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
    # 仮のロジック（本来はここでNLPやDB処理などを行う）
    prompt = (
        "あなたはシステム設計の専門家です。\n"
        "以下の設計詳細をもとに、Mermaid記法のシーケンス図を生成してください。\n"
        "例:\n"
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
        "【Mermaid記法の図】\n"
        "sequenceDiagram\n"
        "    participant ユーザー\n"
        "    participant フロントエンド\n"
        "    participant バックエンド\n"
        "    participant GPT_API\n"
        "    participant MermaidJS\n"
        "\n"
        "    %% ユーザーが設計の概要を入力\n"
        "    ユーザー->>フロントエンド: 設計の概要を入力\n"
        "    %% フロントエンドがバックエンドに入力を送信\n"
        "    フロントエンド->>バックエンド: 入力データを送信\n"
        "    %% バックエンドがGPTのAPIを使用して入力を解析\n"
        "    バックエンド->>GPT_API: 自然言語解析リクエスト\n"
        "    %% GPTのAPIがMermaidフォーマットを返す\n"
        "    GPT_API-->>バックエンド: Mermaidフォーマット\n"
        "    %% バックエンドがフロントエンドにMermaidフォーマットを返す\n"
        "    バックエンド-->>フロントエンド: Mermaidフォーマット\n"
        "    %% フロントエンドがMermaid.jsを使用して図を生成\n"
        "    フロントエンド->>MermaidJS: 図を生成\n"
        "    %% フロントエンドがユーザーに図を表示\n"
        "    MermaidJS-->>フロントエンド: 図のデータ\n"
        "    フロントエンド-->>ユーザー: 図を表示\n"
        "【設計詳細】\n"
        f"{design_detail}\n"
        "【Mermaid記法の図】"
    )
    start = time.time()
    print("=== 推論開始 ===")
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    print(f"トークナイズ完了: {time.time() - start:.2f}秒")
    outputs = model.generate(**inputs, max_new_tokens=1000)
    print(f"モデル推論完了: {time.time() - start:.2f}秒")
    input_length = inputs['input_ids'].shape[1]
    mermaid = tokenizer.decode(outputs[0][input_length:], skip_special_tokens=True)
    print(f"デコード完了: {time.time() - start:.2f}秒")
    # if count is None:
    #     mermaid = """sequenceDiagram
    #     participant ユーザー
    #     participant フロントエンド
    #     participant バックエンド
    #     participant GPT_API
    #     participant MermaidJS

    #     %% ユーザーが設計の概要を入力
    #     ユーザー->>フロントエンド: 設計の概要を入力
    #     %% フロントエンドがバックエンドに入力を送信
    #     フロントエンド->>バックエンド: 入力データを送信
    #     %% バックエンドがGPTのAPIを使用して入力を解析
    #     バックエンド->>GPT_API: 自然言語解析リクエスト
    #     %% GPTのAPIがMermaidフォーマットを返す
    #     GPT_API-->>バックエンド: Mermaidフォーマット
    #     %% バックエンドがフロントエンドにMermaidフォーマットを返す
    #     バックエンド-->>フロントエンド: Mermaidフォーマット
    #     %% フロントエンドがMermaid.jsを使用して図を生成
    #     フロントエンド->>MermaidJS: 図を生成
    #     %% フロントエンドがユーザーに図を表示
    #     MermaidJS-->>フロントエンド: 図のデータ
    #     フロントエンド-->>ユーザー: 図を表示"""
    # elif count == 2:
    #     mermaid = """sequenceDiagram
    #     participant ユーザー2
    #     participant フロントエンド
    #     participant バックエンド
    #     participant GPT_API
    #     participant MermaidJS

    #     %% ユーザーが設計の概要を入力
    #     ユーザー->>フロントエンド: 設計の概要を入力
    #     %% フロントエンドがバックエンドに入力を送信
    #     フロントエンド->>バックエンド: 入力データを送信
    #     %% バックエンドがGPTのAPIを使用して入力を解析
    #     バックエンド->>GPT_API: 自然言語解析リクエスト
    #     %% GPTのAPIがMermaidフォーマットを返す
    #     GPT_API-->>バックエンド: Mermaidフォーマット
    #     %% バックエンドがフロントエンドにMermaidフォーマットを返す
    #     バックエンド-->>フロントエンド: Mermaidフォーマット
    #     %% フロントエンドがMermaid.jsを使用して図を生成
    #     フロントエンド->>MermaidJS: 図を生成
    #     %% フロントエンドがユーザーに図を表示
    #     MermaidJS-->>フロントエンド: 図のデータ
    #     フロントエンド-->>ユーザー: 図を表示"""
    # else:
    #     mermaid = ""
    return mermaid
