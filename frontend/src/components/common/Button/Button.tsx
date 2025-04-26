import React from 'react';
import { ButtonProps } from './types';
import { StyledButton } from './styles';

export const Button: React.FC<ButtonProps> = ({ children, ...props }) => (
  <StyledButton {...props}>{children}</StyledButton>
);
