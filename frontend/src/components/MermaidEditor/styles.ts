import styled from 'styled-components';
import { TextAreaProps } from '../common/TextArea/types';

export const MermaidEditorContainer = styled.div`
  width: 100%;

  height: 100%;
  margin-bottom: 0.5%; /* 親要素の幅に対する割合で設定 */
`;

export const MermaidEditorTextAreaContainer = styled.textarea<TextAreaProps>`
  // TextAreaのスタイル継承がうまくいかなかったため、同じ部分も記載
  width: 100%;
  min-height: ${({ $minRows = 5 }) => {
    return `calc(1.5em * ${$minRows})`;
  }}; /* デフォルトは5行 */
  max-height: ${({ $maxRows = 20 }) => {
    return `calc(1.5em * ${$maxRows})`;
  }}; /* デフォルトは20行 */
  line-height: 1.5em;
  resize: vertical;
  margin-left: 0;
  margin-right: 0;
  box-sizing: border-box;
  resize: vertical;

  background: #282c34;         // コードブロック風の黒色の背景色
  border-radius: 6px;      // 角丸
  padding: 1rem;               // 内側余白
  font-family: 'Fira Mono', 'Consolas', 'Menlo', monospace; // 等幅フォント
  color: #fff;                 // 文字色
`;
