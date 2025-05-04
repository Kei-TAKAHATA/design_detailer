/**
 * 設計の詳細テキストをMermaidフォーマット（シーケンス図やフローチャート等）に変換する
 * @param designDetailText - 設計の詳細テキスト
 * @returns 変換されたMermaid記法のコード（図の種類は内容により異なる）
 */
export async function convertDesignDetailTextToMermaidCode(designDetailText: string): Promise<string> {
    // バックエンドAPIを呼び出して、設計の詳細をMermaidフォーマットに変換
    const response = await fetch('http://127.0.0.1:8000/api/mermaid', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            design_detail: designDetailText,
        }),
    });
    if (!response.ok) {
        throw new Error('APIリクエストに失敗しました');
    }
    const data = await response.json();
    return data.mermaid;
}
