import React, { useEffect, useRef, useState } from 'react';
import mermaid from 'mermaid';
import { MermaidPreviewProps } from './types';
import { StyledMermaidPreview, StyledCopyButton } from './styles';
import debounce from 'lodash.debounce';
import { copySvgToClipboard } from '../../utils/copySvgToClipboard';


export const MermaidPreview: React.FC<MermaidPreviewProps> = ({ mermaidCode }) => {
  const mermaidRef = useRef<HTMLDivElement>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const renderMermaid = debounce(async () => {
      if (mermaidRef.current && mermaidCode.trim() !== '') {
        try {
          // mermaidの初期化
          mermaid.initialize({ startOnLoad: false });
          // ユニークなIDを生成
          const uniqueId = `mermaid-diagram-${Math.random().toString().replace('.', '')}`;
          const { svg } = await mermaid.render(uniqueId, mermaidCode);
          mermaidRef.current.innerHTML = svg;
          setError(null); // エラーがない場合はエラーをクリア
        } catch (error) {
          console.error('Mermaidのレンダリング中にエラーが発生しました: ', error);
          setError('Mermaidコードにエラーがあります。形式を確認してください。');
        }
      }
    }, 500); // 500ミリ秒の遅延

    renderMermaid();

    return () => {
      renderMermaid.cancel();
    };
  }, [mermaidCode]);

  const handleCopy = async () => {
    if (mermaidRef.current) {
      // 拡大しても綺麗に見れるようにSVGで取得
      const svgElement = mermaidRef.current.querySelector('svg');
      if (svgElement) {
        try {
          await copySvgToClipboard(svgElement);
          alert('図がクリップボードに画像としてコピーされました！');
        } catch (err) {
          console.error('クリップボードへのコピーに失敗しました: ', err);
          alert('コピーに失敗しました');
        }
      }
    }
  };

  return (
    <StyledMermaidPreview>
      <div ref={mermaidRef} className="mermaid"></div>
      {error && <div className="error-message">{error}</div>}
      <StyledCopyButton
      onClick={handleCopy}
      children="図をコピー"
      />
    </StyledMermaidPreview>
  );
};
