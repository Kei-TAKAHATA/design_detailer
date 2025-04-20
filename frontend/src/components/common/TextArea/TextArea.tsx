import React from 'react';

import { TextAreaProps } from './types';
import { StyledTextArea } from './styles';

export const TextArea: React.FC<TextAreaProps> = ({ value, onChange, $minRows, $maxRows, $cols, placeholder }) => {

  return (
    <StyledTextArea
      value={value}
      onChange={onChange}
      $minRows={$minRows}
      $maxRows={$maxRows}
      $cols={$cols}
      placeholder={placeholder}
    />
  );
};
