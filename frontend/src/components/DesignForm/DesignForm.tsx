import React from 'react';
import { DesignFormProps } from './types';
import { StyledDesignForm } from './styles';
import { ConvertButton } from './components/ConvertButton';
import { TextArea } from '../common/TextArea';

export const DesignForm: React.FC<DesignFormProps> = ({ onSubmit, value, onChange}) => {
  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault(); // デフォルトのフォーム送信を防ぐ
    onSubmit();
  };

  return (
    <StyledDesignForm onSubmit={handleSubmit} height="8rem">
      <TextArea placeholder="設計の概要を入力してください" value={value} onChange={onChange} />
      <ConvertButton onClick={onSubmit} />
    </StyledDesignForm>
  );
};
