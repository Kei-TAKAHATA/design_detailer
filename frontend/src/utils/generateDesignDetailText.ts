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
export function generateDesignDetailText(designFormText: string): string {
    // バックエンドAPIを呼び出して、設計の詳細を生成
    // 一旦固定のテキストを返す
    const generatedDesignDetailText = `
      1. ユーザーインターフェース (React + TypeScript)
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
      設計の概要と生成された図をまとめて表示するためのロジックを実装。
    `;
    return generatedDesignDetailText;
}
