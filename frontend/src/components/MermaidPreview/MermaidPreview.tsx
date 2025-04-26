import React, { useEffect, useRef, useState } from 'react';
import mermaid from 'mermaid';
import { MermaidPreviewProps } from './types';
import { StyledMermaidPreview, StyledCopyButton } from './styles';
import debounce from 'lodash.debounce';


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

  // const copyToClipboard = () => {
  //   if (mermaidRef.current) {
  //     const svgContent = mermaidRef.current.innerHTML;
  //     navigator.clipboard.writeText(svgContent).then(() => {
  //       alert('図がクリップボードにコピーされました！');
  //     }).catch(err => {
  //       console.error('クリップボードへのコピーに失敗しました: ', err);
  //     });
  //   }
  // };
  // const copyToClipboard = () => {
  //   if (mermaidRef.current) {
  //     const svgElement = mermaidRef.current.querySelector('svg');
  //     if (svgElement) {
  //       const canvas = document.createElement('canvas');
  //       const ctx = canvas.getContext('2d');
  //       const svgData = new XMLSerializer().serializeToString(svgElement);
  //       const img = new Image();
  //       const svgBlob = new Blob([svgData], { type: 'image/svg+xml;charset=utf-8' });
  //       const url = URL.createObjectURL(svgBlob);

  //       img.onload = () => {
  //         canvas.width = img.width;
  //         canvas.height = img.height;
  //         ctx?.drawImage(img, 0, 0);
  //         canvas.toBlob((blob) => {
  //           if (blob) {
  //             const item = new ClipboardItem({ 'image/png': blob });
  //             navigator.clipboard.write([item]).then(() => {
  //               alert('図がクリップボードに画像としてコピーされました！');
  //             }).catch(err => {
  //               console.error('クリップボードへのコピーに失敗しました: ', err);
  //             });
  //           }
  //         });
  //         URL.revokeObjectURL(url);
  //       };
  //       img.src = url;
  //     }
  //   }
  // };

  const copyToClipboard = () => {
    if (mermaidRef.current) {
      const svgElement = mermaidRef.current.querySelector('svg');
      if (svgElement) {
        const canvas = document.createElement('canvas');
        const ctx = canvas.getContext('2d');
        const svgData = new XMLSerializer().serializeToString(svgElement);
        const img = new Image();
        const svgBlob = new Blob([svgData], { type: 'image/svg+xml;charset=utf-8' });
        const url = URL.createObjectURL(svgBlob);

        img.onload = () => {
          // SVGのviewBox属性を使用してサイズを設定
          const viewBox = svgElement.getAttribute('viewBox');
          if (viewBox) {
            const [minX, minY, width, height] = viewBox.split(' ').map(Number);
            canvas.width = width;
            canvas.height = height;
          } else {
            // viewBoxがない場合は、デフォルトのサイズを使用
            canvas.width = img.width;
            canvas.height = img.height;
          }

          ctx?.drawImage(img, 0, 0);
          canvas.toBlob((blob) => {
            if (blob) {
              const item = new ClipboardItem({ 'image/png': blob });
              navigator.clipboard.write([item]).then(() => {
                alert('図がクリップボードに画像としてコピーされました！');
              }).catch(err => {
                console.error('クリップボードへのコピーに失敗しました: ', err);
              });
            }
          });
          URL.revokeObjectURL(url);
        };
        img.src = url;
      }
    }
  };

  return (
    <StyledMermaidPreview>
      <div ref={mermaidRef} className="mermaid"></div>
      {error && <div className="error-message">{error}</div>}
      <StyledCopyButton
      onClick={copyToClipboard}
      children="図をコピー"
      />
    </StyledMermaidPreview>
  );
};
