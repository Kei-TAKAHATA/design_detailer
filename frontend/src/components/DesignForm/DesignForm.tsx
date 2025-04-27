import React from 'react';
import { DesignFormProps } from './types';
import { DesignFormContainer, ConvertButtonContainer } from './styles';
import { TextArea } from '../common/TextArea';


export const DesignForm: React.FC<DesignFormProps> = ({ onSubmit, value, onChange}) => {
  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault(); // デフォルトのフォーム送信を防ぐ
    onSubmit();
  };

  return (
    <DesignFormContainer onSubmit={handleSubmit} height="8rem">
      <TextArea
        placeholder="設計の概要を入力してください"
        value={value}
        onChange={onChange}
        $minRows={1}
      />
      <ConvertButtonContainer
        onClick={onSubmit}
        children="設計を生成"
      />
    </DesignFormContainer>
  );
};
