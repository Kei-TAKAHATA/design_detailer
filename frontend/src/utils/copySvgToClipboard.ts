export const copySvgToClipboard = async (svgElement: SVGSVGElement): Promise<void> => {
    return new Promise((resolve, reject) => {
      const canvas = document.createElement('canvas');
      const ctx = canvas.getContext('2d');
      const svgData = new XMLSerializer().serializeToString(svgElement);
      const img = new Image();
      const svgBlob = new Blob([svgData], { type: 'image/svg+xml;charset=utf-8' });
      const url = URL.createObjectURL(svgBlob);

      img.onload = () => {
        const viewBox = svgElement.getAttribute('viewBox');
        if (viewBox) {
          const [minX, minY, width, height] = viewBox.split(' ').map(Number);
          canvas.width = width;
          canvas.height = height;
        } else {
          canvas.width = img.width;
          canvas.height = img.height;
        }

        ctx?.drawImage(img, 0, 0);
        canvas.toBlob((blob) => {
          if (blob) {
            const item = new ClipboardItem({ 'image/png': blob });
            navigator.clipboard.write([item]).then(resolve).catch(reject);
          } else {
            reject(new Error('Blob作成に失敗しました'));
          }
        });
        URL.revokeObjectURL(url);
      };
      img.onerror = reject;
      img.src = url;
    });
  };
