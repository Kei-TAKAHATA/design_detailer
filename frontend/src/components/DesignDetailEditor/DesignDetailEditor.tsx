import React, { useState, useEffect } from 'react';
import { DesignDetailEditorProps } from './types';
import { StyledDesignDetailEditor, StyledUpdateButton } from './styles';
import { TextArea } from '../common/TextArea';


export const DesignDetailEditor: React.FC<DesignDetailEditorProps> = ({ onSubmit, designDetailText, onChange }) => {
  const [lineCount, setLineCount] = useState(designDetailText.split('\n').length);

  useEffect(() => {
    setLineCount(designDetailText.split('\n').length);
  }, [designDetailText]);

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault(); // デフォルトのフォーム送信を防ぐ
    onSubmit();
  };

  return (
    <StyledDesignDetailEditor onSubmit={handleSubmit}>
      <TextArea
        placeholder="設計の詳細を入力してください"
        value={designDetailText}
        onChange={onChange}
        $minRows={Math.max(lineCount + 1, 5)} // 行数を設定、最低でも5行
      />
      <StyledUpdateButton
        onClick={onSubmit}
        children="詳細を更新"
      />
    </StyledDesignDetailEditor>
  );
};
