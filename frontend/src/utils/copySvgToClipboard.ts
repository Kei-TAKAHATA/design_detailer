/**
 * SVG要素をPNG画像としてクリップボードにコピーするユーティリティ関数
 *
 * SVGはそのままクリップボードAPIで扱えないため、Canvasに描画してPNGに変換し、
 * そのPNG画像をクリップボードにコピーします。
 *
 * @param svgElement - コピー対象のSVG要素
 * @returns Promise<void> コピー完了時にresolve、失敗時にreject
 */
export const copySvgToClipboard = async (svgElement: SVGSVGElement): Promise<void> => {
    return new Promise((resolve, reject) => {
      // SVGをPNG画像としてクリップボードにコピーするための処理

      // 1. SVG（ベクトル画像）をラスター画像（ピクセルの集まりの画像）化するためキャンバス要素を作成
      // ベクトル画像: 線や図形の形状を定義するもの。拡大しても綺麗に見れる。
      // ラスター画像: ピクセルの集まりの画像。拡大するとピクセルが粗くなる。
      const canvas = document.createElement('canvas');
      const ctx = canvas.getContext('2d');

      // 2. SVG要素を文字列に変換（シリアライズ）
      // シリアライズ: オブジェクトをテキストデータに変換すること
      const svgData = new XMLSerializer().serializeToString(svgElement);
      const img = new Image();

      // 3. SVGデータをBlob化し、URLを生成（Image要素で読み込むため）
      // Blob化: テキストやデータを「ファイルのようなバイナリデータ」として扱うこと
      const svgBlob = new Blob([svgData], { type: 'image/svg+xml;charset=utf-8' });
      const url = URL.createObjectURL(svgBlob);

      // 4. 画像として読み込まれたら
      img.onload = () => {
        // SVGのviewBox属性からサイズを取得し、キャンバスサイズをSVGと同じに設定
        // （viewBoxがない場合は画像サイズをそのまま使う）
        // viewBox: SVGのサイズを定義する属性。SVGのサイズを指定することで、SVGを拡大しても綺麗に見れる。
        // 多くのSVG生成ライブラリは、適切なviewBoxを自動で設定してくれる。
        const viewBox = svgElement.getAttribute('viewBox');
        if (viewBox) {
          const [minX, minY, width, height] = viewBox.split(' ').map(Number);
          canvas.width = width;
          canvas.height = height;
        } else {
          canvas.width = img.width;
          canvas.height = img.height;
        }

        // 5. キャンバスにSVG画像を描画（ここでSVG→PNG変換が行われる）
        ctx?.drawImage(img, 0, 0);

        // 6. キャンバスの内容をPNG Blobとして取得し、クリップボードにコピー
        // Clipboard APIはSVGを直接扱えないためPNGに変換している
        // ClipboardItem: クリップボードに保存するデータの形式を指定するオブジェクト
        canvas.toBlob((blob) => {
          if (blob) {
            const item = new ClipboardItem({ 'image/png': blob });
            navigator.clipboard.write([item]).then(resolve).catch(reject);
          } else {
            reject(new Error('Blob作成に失敗しました'));
          }
        });

        // 7. 一時的に生成したURLを解放（メモリリーク防止）
        // revokeObjectURL: URLを解放するメソッド
        URL.revokeObjectURL(url);
      };

      // 画像の読み込みエラー時の処理
      // onerror: 画像の読み込みエラー時に発火するイベントハンドラ
      img.onerror = reject;

      // 画像のソースにSVGのURLを設定（これでimg.onloadが発火する）
      img.src = url;
    });
  };
