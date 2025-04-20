import React from 'react';
import { DesignFormProps } from './types';
import { Button } from '../common/Button';

export const DesignForm: React.FC<DesignFormProps> = ({ onSubmit }) => {
  return (
    <div>
      <textarea placeholder="設計の概要を入力してください"></textarea>
      <Button onClick={() => {}}>変換</Button>
    </div>
  );
};
