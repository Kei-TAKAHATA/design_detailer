import React, { useState } from 'react';
import { AppTitle } from './components/AppTitle';
import { DesignForm } from './components/DesignForm';
import { DesignDetailEditor } from './components/DesignDetailEditor';
import { MermaidEditor } from './components/MermaidEditor';
import { MermaidPreview } from './components/MermaidPreview';
import { generateDesignDetailText } from './utils/generateDesignDetailText';
import { convertDesignDetailTextToMermaidCode } from './utils/convertDesignDetailTextToMermaidCode';

export const App: React.FC = () => {
  // 概要の入力欄のテキスト管理
  const [designFormText, setDesignFormText] = useState('');
  // 設計の詳細のテキスト管理
  const [designDetailText, setDesignDetailText] = useState('');
  // Mermaidのコード
  const [mermaidCode, setMermaidCode] = useState('');

  // 概要の入力欄のテキスト変更時の処理
  const handleDesignFormChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
    setDesignFormText(event.target.value);
  };

  // 詳細の入力欄のテキスト変更時の処理
  const handleDesignDetailEditorChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
    setDesignDetailText(event.target.value);
  };

  // 概要入力ボタンを押した時の処理
  const handleConvertButtonClick = async () => {
    // 概要の入力欄のテキストから詳細を生成
    const generatedDesignDetailText = await generateDesignDetailText(designFormText);
    setDesignDetailText(generatedDesignDetailText);

    // 詳細の文章からMermaidのコードに変換
    const newMermaidCode = await convertDesignDetailTextToMermaidCode(generatedDesignDetailText);
    setMermaidCode(newMermaidCode);
  };

  // 詳細入力ボタンを押した時の処理
  const handleDesignDetailEditorSubmit = async () => {
    // 詳細の文章からMermaidのコードに変換
    const newMermaidCode = await convertDesignDetailTextToMermaidCode(designDetailText, 2);
    setMermaidCode(newMermaidCode);
  };

  return (
    <div>
      <AppTitle title="Design Note"/>
      <DesignForm
        onSubmit={handleConvertButtonClick}
        value={designFormText}
        onChange={handleDesignFormChange}
      />
      <DesignDetailEditor
        onSubmit={handleDesignDetailEditorSubmit}
        designDetailText={designDetailText}
        onChange={handleDesignDetailEditorChange}
      />
      <MermaidEditor
        code={mermaidCode}
        onChange={setMermaidCode}
      />
      <MermaidPreview mermaidCode={mermaidCode} />
    </div>
  );
};
