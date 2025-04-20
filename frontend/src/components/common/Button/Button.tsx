import React from 'react';
import { ButtonProps } from './types';
import { StyledButton } from './styles';

export const Button: React.FC<ButtonProps> = ({ children, onClick }) => {
  return (
    <StyledButton onClick={onClick}>
      {children}
    </StyledButton>
  );
};
