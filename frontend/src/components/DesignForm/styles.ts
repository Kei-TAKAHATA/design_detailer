import styled from "styled-components";
import { Button } from "../common/Button";


export const StyledDesignForm = styled.div<{ height?: string }>`
  display: flex;
  flex-direction: row;
  gap: 2%; /* gapが余白を作っている可能性があるので確認 */

  height: ${(props) => props.height || 'auto'};
  width: 100%;
  writing-mode: horizontal-tb; /* 横書きに設定 */
  text-orientation: mixed; /* 通常の文字方向に設定 */
  // margin: 0 auto;
  margin-bottom: 2%; /* 親要素の幅に対する割合で設定 */
  margin-left: 0;  /* 左側のマージンを0に設定 */
  margin-right: 0; /* 右側のマージンを0に設定 */
`;

// export const StyledDesignFormTextArea = styled(TextArea)`
//   background: #444;         // コードブロック風のグレー背景色
//   border-radius: 6px;      // 角丸
//   padding: 1rem;               // 内側余白
//   font-family: 'Fira Mono', 'Consolas', 'Menlo', monospace; // 等幅フォント
//   color: #fff;                 // 文字色
// `;


export const StyledConvertButton = styled(Button)`
  height: 100%; /* 親要素の高さに合わせる */
  width: 20%;
  padding: 0.5rem 4rem; /* ボタンの内側の余白を設定 */
  margin-left: auto; /* 右揃えにするための設定 */
`;
