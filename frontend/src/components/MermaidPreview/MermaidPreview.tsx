import React, { useEffect, useRef } from 'react';
import mermaid from 'mermaid';
import { MermaidPreviewProps } from './types';
import { StyledMermaidPreview } from './styles';
export const MermaidPreview: React.FC<MermaidPreviewProps> = ({ mermaidCode }) => {
  const mermaidRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const renderMermaid = async () => {
      if (mermaidRef.current &&  mermaidCode.trim() !== '') {
        // mermaidの初期化
        mermaid.initialize({ startOnLoad: false });
        // ユニークなIDを生成
        const uniqueId = `mermaid-diagram-${Math.random().toString().replace('.', '')}`;
        const { svg } = await mermaid.render(uniqueId, mermaidCode);
        mermaidRef.current.innerHTML = svg;
      }
    };

    renderMermaid();
  }, [mermaidCode]);

  return (
    <StyledMermaidPreview>
      <div ref={mermaidRef} className="mermaid"></div>
    </StyledMermaidPreview>
  );
};
