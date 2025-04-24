import React from 'react';
import { DesignDetailEditorProps } from './types';
import { StyledDesignDetailEditor } from './styles';
import { TextArea } from '../common/TextArea';

export const DesignDetailEditor: React.FC<DesignDetailEditorProps> = ({ onSubmit, designDetailText, onChange }) => {
  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault(); // デフォルトのフォーム送信を防ぐ
    onSubmit();
  };

  return (
    <StyledDesignDetailEditor onSubmit={handleSubmit}>
      <TextArea placeholder="設計の詳細を入力してください" value={designDetailText} onChange={onChange} />
    </StyledDesignDetailEditor>
  );
};