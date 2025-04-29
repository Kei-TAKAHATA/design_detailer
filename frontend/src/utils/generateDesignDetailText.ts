/**
 * 概要テキスト（設計の要約）から、設計詳細テキスト（より具体的な設計内容）を生成する
 *
 * @param designFormText - ユーザーが入力した設計の概要テキスト
 * @returns 設計詳細テキスト（設計の各要素や手順が記述された文字列）
 *
 * @example
 * const detail = generateDesignDetailText("ユーザー認証機能を追加したい");
 * // detail: "1. ユーザーインターフェース ... 2. バックエンドロジック ... "
 */
export async function generateDesignDetailText(designFormText: string): Promise<string> {
    // バックエンドAPIを呼び出して、設計の詳細を生成
    const response = await fetch('http://127.0.0.1:8000/api/design_detail', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          design_summary: designFormText
        }),
    });
    if (!response.ok) {
        throw new Error('APIリクエストに失敗しました');
    }
    const data = await response.json();
    return data.design_detail;
}
