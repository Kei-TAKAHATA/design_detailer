import React, { useState, useEffect } from 'react';
import { MermaidEditorProps } from './types';
import { MermaidEditorContainer, MermaidEditorTextAreaContainer } from './styles';


export const MermaidEditor: React.FC<MermaidEditorProps> = ({ code, onChange }) => {
  const [lineCount, setLineCount] = useState(code.split('\n').length);

  useEffect(() => {
    setLineCount(code.split('\n').length);
  }, [code]);

  return (
    <MermaidEditorContainer>
      <MermaidEditorTextAreaContainer
        value={code}
        onChange={(event) => onChange(event.target.value)}
        $minRows={Math.max(lineCount + 1, 5)}
        $maxRows={20}
        $cols={50}
        placeholder="Mermaidのコードを入力してください"
      />
    </MermaidEditorContainer>
  );
};