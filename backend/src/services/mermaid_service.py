def convert_design_detail_to_mermaid(design_detail: str, count: int | None = None) -> str:
    # 仮のロジック（本来はここでNLPやDB処理などを行う）
    if count is None:
        mermaid = """sequenceDiagram
        participant ユーザー
        participant フロントエンド
        participant バックエンド
        participant GPT_API
        participant MermaidJS

        %% ユーザーが設計の概要を入力
        ユーザー->>フロントエンド: 設計の概要を入力
        %% フロントエンドがバックエンドに入力を送信
        フロントエンド->>バックエンド: 入力データを送信
        %% バックエンドがGPTのAPIを使用して入力を解析
        バックエンド->>GPT_API: 自然言語解析リクエスト
        %% GPTのAPIがMermaidフォーマットを返す
        GPT_API-->>バックエンド: Mermaidフォーマット
        %% バックエンドがフロントエンドにMermaidフォーマットを返す
        バックエンド-->>フロントエンド: Mermaidフォーマット
        %% フロントエンドがMermaid.jsを使用して図を生成
        フロントエンド->>MermaidJS: 図を生成
        %% フロントエンドがユーザーに図を表示
        MermaidJS-->>フロントエンド: 図のデータ
        フロントエンド-->>ユーザー: 図を表示"""
    elif count == 2:
        mermaid = """sequenceDiagram
        participant ユーザー2
        participant フロントエンド
        participant バックエンド
        participant GPT_API
        participant MermaidJS

        %% ユーザーが設計の概要を入力
        ユーザー->>フロントエンド: 設計の概要を入力
        %% フロントエンドがバックエンドに入力を送信
        フロントエンド->>バックエンド: 入力データを送信
        %% バックエンドがGPTのAPIを使用して入力を解析
        バックエンド->>GPT_API: 自然言語解析リクエスト
        %% GPTのAPIがMermaidフォーマットを返す
        GPT_API-->>バックエンド: Mermaidフォーマット
        %% バックエンドがフロントエンドにMermaidフォーマットを返す
        バックエンド-->>フロントエンド: Mermaidフォーマット
        %% フロントエンドがMermaid.jsを使用して図を生成
        フロントエンド->>MermaidJS: 図を生成
        %% フロントエンドがユーザーに図を表示
        MermaidJS-->>フロントエンド: 図のデータ
        フロントエンド-->>ユーザー: 図を表示"""
    else:
        mermaid = ""
    return mermaid
