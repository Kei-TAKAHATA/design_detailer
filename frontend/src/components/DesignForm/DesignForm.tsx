import React from 'react';
import { DesignFormProps } from './types';

export const DesignForm: React.FC<DesignFormProps> = ({ onSubmit }) => {
  return (
    <div>
      <textarea placeholder="設計の概要を入力してください"></textarea>
      <button>変換</button>
    </div>
  );
};
