import React from 'react';
import { MermaidPreviewProps } from './types';

export const MermaidPreview: React.FC<MermaidPreviewProps> = ({ mermaidCode }) => {
  return (
    <div>
      <h2>Mermaid Diagram Preview</h2>
      <div id="mermaid-diagram"></div>
    </div>
  );
};
