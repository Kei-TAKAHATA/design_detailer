import React from 'react';
import { StyledConvertButton } from './styles';
import { ConvertButtonProps } from './types';

export const ConvertButton: React.FC<ConvertButtonProps> = ({ onClick }) => {
  return (
    <StyledConvertButton onClick={onClick}>変換</StyledConvertButton>
  );
};
