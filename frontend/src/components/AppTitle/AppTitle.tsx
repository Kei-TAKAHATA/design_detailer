import React from 'react';
import { AppTitleProps } from './types';
import { StyledAppTitle } from './styles';

export const AppTitle: React.FC<AppTitleProps> = ({ title, icon }) => (
  <StyledAppTitle>
    {icon && <span role="img" aria-label="設計図">{icon}</span>} {title}
  </StyledAppTitle>
);
