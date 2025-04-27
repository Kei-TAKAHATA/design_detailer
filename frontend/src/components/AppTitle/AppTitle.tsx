import React from 'react';
import { AppTitleProps } from './types';
import { AppTitleContainer } from './styles';

export const AppTitle: React.FC<AppTitleProps> = ({ title, icon }) => (
  <AppTitleContainer>
    {icon && <span role="img" aria-label="設計図">{icon}</span>} {title}
  </AppTitleContainer>
);
