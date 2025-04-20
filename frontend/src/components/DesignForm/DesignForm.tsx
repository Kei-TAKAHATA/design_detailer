import React from 'react';
import { DesignFormProps } from './types';
import { ConvertButton } from './components/ConvertButton';

export const DesignForm: React.FC<DesignFormProps> = ({ onSubmit, value, onChange}) => {
  return (
    <div>
      <textarea placeholder="設計の概要を入力してください" value={value} onChange={onChange}></textarea>
      <ConvertButton onClick={onSubmit} />
    </div>
  );
};
