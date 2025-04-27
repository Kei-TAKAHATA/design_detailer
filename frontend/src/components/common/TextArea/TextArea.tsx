import React from 'react';

import { TextAreaProps } from './types';
import { TextAreaContainer } from './styles';

export const TextArea: React.FC<TextAreaProps> = (props) => {
  return <TextAreaContainer {...props} />;
};
