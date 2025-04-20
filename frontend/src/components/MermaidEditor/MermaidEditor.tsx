import React from 'react';
import { MermaidEditorProps } from './types';
import { StyledMermaidEditor } from './styles';
import { TextArea } from '../common/TextArea';

export const MermaidEditor: React.FC<MermaidEditorProps> = ({ code, onChange }) => {
  return (
    <StyledMermaidEditor>
      <TextArea
        value={code}
        onChange={(event) => onChange(event.target.value)}
        $minRows={5}
        $maxRows={20}
        $cols={50}
        placeholder="Mermaidのコードを入力してください"
        // style={{ width: '100%', marginBottom: '20px' }}
      />
    </StyledMermaidEditor>
  );
};