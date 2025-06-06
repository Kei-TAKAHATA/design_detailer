import React from 'react';
import { ButtonProps } from './types';
import { ButtonContainer } from './styles';

export const Button: React.FC<ButtonProps> = ({ children, ...props }) => (
  <ButtonContainer {...props}>{children}</ButtonContainer>
);
