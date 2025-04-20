import React from 'react';
import { ConvertButtonContainer } from './styles';
import { ConvertButtonProps } from './types';

export const ConvertButton: React.FC<ConvertButtonProps> = ({ onClick }) => {
  return (
    <ConvertButtonContainer onClick={onClick}>変換</ConvertButtonContainer>
  );
};
