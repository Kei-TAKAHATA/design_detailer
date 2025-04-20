import React from 'react';
import { MermaidEditorProps } from './types';
import { MermaidEditorContainer } from './styles';
import { TextArea } from '../common/TextArea';

export const MermaidEditor: React.FC<MermaidEditorProps> = ({ code, onChange }) => {
  return (
    <MermaidEditorContainer>
      <TextArea
        value={code}
        onChange={(event) => onChange(event.target.value)}
        $minRows={5}
        $maxRows={20}
        $cols={50}
        placeholder="Mermaidのコードを入力してください"
        // style={{ width: '100%', marginBottom: '20px' }}
      />
    </MermaidEditorContainer>
  );
};