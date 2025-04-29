def generate_design_detail(design_summary: str) -> str:
    # 仮のロジック（本来はここでNLPやDB処理などを行う）
    # detail = f"『{summary}』の詳細設計（ここに生成ロジックを追加）"
    design_detail = """1. ユーザーインターフェース (React + TypeScript)
      入力コンポーネント:
      設計の概要を入力するためのテキストエリア。
      出力コンポーネント:
      変換されたMermaidフォーマットを表示するエリア。
      Mermaid.jsを使用して生成された図を表示するエリア。
      設計の概要と図をまとめて表示するエリア。
      ボタンコンポーネント:
      「変換」ボタン: 設計の概要をMermaidフォーマットに変換し、図を生成する。
      「出力」ボタン: 設計の概要と生成された図をまとめて表示する。
      2. バックエンドロジック
      入力解析:
      ユーザーの入力を解析し、Mermaidフォーマットに変換するロジックを実装。
      GPTのAPIを使用して自然言語を解析し、適切なMermaidコードを生成。
      3. フロントエンドロジック (React + TypeScript)
      Mermaidの統合:
      Mermaid.jsを使用して、Mermaidフォーマットから図を生成。
      生成された図をユーザーインターフェースに表示。
      出力の統合:
      設計の概要と生成された図をまとめて表示するためのロジックを実装。"""
    return design_detail
