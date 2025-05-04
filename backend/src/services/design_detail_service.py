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
    # 設計の概要から詳細を生成する処理
    prompt = (
        "あなたはシステム設計の専門家です。\n"
        "以下の設計概要をもとに、設計詳細を日本語で3つ以上の箇条書きで出力してください。\n"
        "例1:\n"
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
        "\n"
        "例2:\n"
        "【設計概要】\n"
        "会議の音声やテキストをアップロードするだけで、AIが自動的に議事録を作成し、要点やアクションアイテムを抽出してくれるツール\n"
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
        "\n"
        "【設計概要】\n"
        f"{design_summary}\n"
        "【設計詳細】"
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
        design_detail = tokenizer.decode(outputs[0][input_length:], skip_special_tokens=True)
        print(f"デコード完了: {time.time() - start:.2f}秒")
    else:
        # llama_cppのモデルを使用する場合
        outputs = model(prompt, max_tokens=1000)
        print(f"モデル推論完了: {time.time() - start:.2f}秒")
        design_detail = outputs["choices"][0]["text"]

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
