/**
 * 設計の詳細テキストをMermaidフォーマット（シーケンス図やフローチャート等）に変換する
 * @param designDetailText - 設計の詳細テキスト
 * @returns 変換されたMermaid記法のコード（図の種類は内容により異なる）
 */
export async function convertDesignDetailTextToMermaidCode(designDetailText: string, count?: number): Promise<string> {
    // バックエンドAPIを呼び出して、設計の詳細をMermaidフォーマットに変換
    // 一旦固定のテキストを返す
    // const generatedMermaidCode = `sequenceDiagram
    // participant ユーザー
    // participant フロントエンド
    // participant バックエンド
    // participant GPT_API
    // participant MermaidJS

    // %% ユーザーが設計の概要を入力
    // ユーザー->>フロントエンド: 設計の概要を入力
    // %% フロントエンドがバックエンドに入力を送信
    // フロントエンド->>バックエンド: 入力データを送信
    // %% バックエンドがGPTのAPIを使用して入力を解析
    // バックエンド->>GPT_API: 自然言語解析リクエスト
    // %% GPTのAPIがMermaidフォーマットを返す
    // GPT_API-->>バックエンド: Mermaidフォーマット
    // %% バックエンドがフロントエンドにMermaidフォーマットを返す
    // バックエンド-->>フロントエンド: Mermaidフォーマット
    // %% フロントエンドがMermaid.jsを使用して図を生成
    // フロントエンド->>MermaidJS: 図を生成
    // %% フロントエンドがユーザーに図を表示
    // MermaidJS-->>フロントエンド: 図のデータ
    // フロントエンド-->>ユーザー: 図を表示`
    // if (count === 2) {
    //     const generatedMermaidCode2 = `sequenceDiagram
    // participant ユーザー2
    // participant フロントエンド
    // participant バックエンド
    // participant GPT_API
    // participant MermaidJS

    // %% ユーザーが設計の概要を入力
    // ユーザー->>フロントエンド: 設計の概要を入力
    // %% フロントエンドがバックエンドに入力を送信
    // フロントエンド->>バックエンド: 入力データを送信
    // %% バックエンドがGPTのAPIを使用して入力を解析
    // バックエンド->>GPT_API: 自然言語解析リクエスト
    // %% GPTのAPIがMermaidフォーマットを返す
    // GPT_API-->>バックエンド: Mermaidフォーマット
    // %% バックエンドがフロントエンドにMermaidフォーマットを返す
    // バックエンド-->>フロントエンド: Mermaidフォーマット
    // %% フロントエンドがMermaid.jsを使用して図を生成
    // フロントエンド->>MermaidJS: 図を生成
    // %% フロントエンドがユーザーに図を表示
    // MermaidJS-->>フロントエンド: 図のデータ
    // フロントエンド-->>ユーザー: 図を表示`
    //     return generatedMermaidCode2
    // }
    console.log("designDetailText", designDetailText);
    console.log("count", count);
    const response = await fetch('http://127.0.0.1:8000/api/mermaid', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            design_detail: designDetailText,
            count: count
        }),
    });
    if (!response.ok) {
        throw new Error('APIリクエストに失敗しました');
    }
    const data = await response.json();
    console.log("data", data);
    return data.mermaid;
}
