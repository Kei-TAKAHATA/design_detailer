import React, { useState } from 'react';
// import mermaid from 'mermaid';
import { DesignForm } from './components/DesignForm';
import { MermaidEditor } from './components/MermaidEditor';
import { MermaidPreview } from './components/MermaidPreview';
import { OutputDisplay } from './components/OutputDisplay';


export const App: React.FC = () => {
  // 概要の入力欄のテキスト管理
  const [designFormText, setDesignFormText] = useState('');
  // Mermaidのコード
  const [mermaidCode, setMermaidCode] = useState('');
  // 出力欄のテキスト管理
  const [outputDisplayText, setOutputDisplayText] = useState('');

  // 概要の入力欄のテキスト変更時の処理
  const handleDesignFormChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
    setDesignFormText(event.target.value);
  };

  // 変換ボタンを押した時の処理
  const handleConvertButtonClick = () => {
    // 概要の入力欄のテキストをMermaidのコードに変換
    // ここでバックエンドAPIを呼び出して、設計の概要をMermaidフォーマットに変換
    // 例として固定のMermaidコードを使用
    const generatedMermaidCode = `sequenceDiagram
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
    フロントエンド-->>ユーザー: 図を表示`;

    // const generatedMermaidCode = convertDesignFormTextToMermaidCode(designFormText);
    setMermaidCode(generatedMermaidCode);
  };


  return (
    <div>
      <h2>設計を作成するツールだよー</h2>
      <DesignForm onSubmit={handleConvertButtonClick} value={designFormText} onChange={handleDesignFormChange} />
      <MermaidEditor code={mermaidCode} onChange={setMermaidCode} />
      <MermaidPreview mermaidCode={mermaidCode} />
      {/* <OutputDisplay designSummary={''} designDiagram={''} /> */}
    </div>
  );
};

// 一旦ここにhooksを作成（後で別ファイルに移す）
const convertDesignFormTextToMermaidCode = (designFormText: string) => {
  // ここに変換ロジックを実装
  return `graph TD;\n${designFormText}`;
};
