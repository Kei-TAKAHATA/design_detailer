import React from 'react';

import { TextAreaProps } from './types';
import { StyledTextArea } from './styles';

export const TextArea: React.FC<TextAreaProps> = (props) => {
  return <StyledTextArea {...props} />;
};
