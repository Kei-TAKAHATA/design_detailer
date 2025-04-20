import React, { useEffect, useRef } from 'react';
import mermaid from 'mermaid';
import { MermaidPreviewProps } from './types';

export const MermaidPreview: React.FC<MermaidPreviewProps> = ({ mermaidCode }) => {
  const mermaidRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const renderMermaid = async () => {
      if (mermaidRef.current) {
        // mermaidの初期化
        mermaid.initialize({ startOnLoad: false });
        // ユニークなIDを生成
        const uniqueId = `mermaid-diagram-${Math.random().toString().replace('.', '')}`;
        // const uniqueId = `mermaid-diagram-${Math.random()}`;
        const { svg } = await mermaid.render(uniqueId, mermaidCode);
        mermaidRef.current.innerHTML = svg;
        // mermaid.render(uniqueId, mermaidCode, (svgCode: string, bindFunctions: (element: Element) => void) => {
        //   if (mermaidRef.current) {
        //     mermaidRef.current.innerHTML = svgCode;
        //     bindFunctions(mermaidRef.current); // 必要に応じてバインド関数を呼び出す
        //   }
        // });
      }
    };

    renderMermaid();
  }, [mermaidCode]);

  return (
    <div>
      <h2>Mermaid Diagram Preview</h2>
      <textarea
        value={mermaidCode}
        readOnly
        rows={10}
        cols={50}
        style={{ width: '100%', marginBottom: '20px' }}
      />
      <div ref={mermaidRef} className="mermaid"></div>
    </div>
  );
};
