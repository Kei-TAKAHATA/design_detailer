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
    # 設計詳細をMermaid記法の図に変換する処理
    prompt = (
        "あなたはシステム設計の専門家です。\n"
        "以下の設計詳細をもとに、Mermaid記法のシーケンス図を生成してください。\n"
        "出力はMermaid記法のコードのみで、説明やコメントは不要です。\n"
        "participant名（登場人物やシステム名）は必ず日本語で記述してください。\n"
        "例1:\n"
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
        "\n"
        "例2:\n"
        "【設計詳細】\n"
        "1. ユーザーインターフェース (React + TypeScript)\n"
        "   アップロードコンポーネント：会議音声ファイル（mp3, wav等）やテキストファイルをアップロードするためのUI。\n"
        "   プログレスバー：音声解析や議事録生成の進捗を表示。\n"
        "   結果表示エリア：生成された議事録、要点、アクションアイテムを見やすく表示。\n"
        "   ダウンロードボタン：議事録や要点をテキストやPDFでダウンロード可能にする。\n"
        "2. バックエンドロジック\n"
        "   音声認識：アップロードされた音声ファイルをテキストに変換（例：Google Speech-to-Text APIやWhisper等を利用）。\n"
        "   議事録生成：変換されたテキストやアップロードされたテキストから、AI（GPT等）を用いて議事録を自動生成。\n"
        "   要点・アクションアイテム抽出：AIが議事録から要点やアクションアイテムを抽出し、分類して返却。\n"
        "   ファイル管理：アップロードファイルや生成結果の一時保存・管理。\n"
        "3. フロントエンドロジック (React + TypeScript)\n"
        "   結果の整形・表示：AIから返却された議事録・要点・アクションアイテムを見やすい形式で表示。\n"
        "   エラーハンドリング：アップロード失敗や解析失敗時のエラーメッセージ表示。\n"
        "   ダウンロード機能：ユーザーが生成結果を簡単にダウンロードできるようにする。\n"
        "【Mermaid記法の図】\n"
        "sequenceDiagram\n"
        "    participant ユーザー\n"
        "    participant フロントエンド\n"
        "    participant バックエンド\n"
        "    participant 音声認識サービス\n"
        "    participant AI（議事録・要点抽出）\n"
        "\n"
        "    ユーザー->>フロントエンド: 音声/テキストファイルをアップロード\n"
        "    フロントエンド->>バックエンド: ファイルを送信\n"
        "    alt 音声ファイルの場合\n"
        "        バックエンド->>音声認識サービス: 音声ファイルをテキストに変換依頼\n"
        "        音声認識サービス-->>バックエンド: テキストデータ返却\n"
        "        バックエンド->>AI（議事録・要点抽出）: テキストデータを送信し議事録生成・要点抽出依頼\n"
        "    else テキストファイルの場合\n"
        "        バックエンド->>AI（議事録・要点抽出）: テキストデータを送信し議事録生成・要点抽出依頼\n"
        "    end\n"
        "    AI（議事録・要点抽出）-->>バックエンド: 議事録・要点・アクションアイテム返却\n"
        "    バックエンド->>フロントエンド: 結果データ返却\n"
        "    フロントエンド->>ユーザー: 議事録・要点・アクションアイテムを表示／ダウンロード\n"
        "\n"
        "【設計詳細】\n"
        f"{design_detail}\n"
        "【Mermaid記法の図】"
    )
    start = time.time()
    print("=== 推論開始 ===")
    if tokenizer:
        # transformersのモデルを使用する場合
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
        print(f"トークナイズ完了: {time.time() - start:.2f}秒")
        outputs = model.generate(**inputs, max_new_tokens=1000)
        print(f"モデル推論完了: {time.time() - start:.2f}秒")
        input_length = inputs['input_ids'].shape[1]
        mermaid = tokenizer.decode(outputs[0][input_length:], skip_special_tokens=True)
        print(f"デコード完了: {time.time() - start:.2f}秒")
    else:
        # llama_cppのモデルを使用する場合
        outputs = model(prompt, max_tokens=1000)
        print(f"モデル推論完了: {time.time() - start:.2f}秒")
        mermaid = outputs["choices"][0]["text"]

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
