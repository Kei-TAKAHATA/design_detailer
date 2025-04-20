import styled from "styled-components";

export const StyledDesignForm = styled.div<{ height?: string }>`
  display: flex;
  flex-direction: row;
  gap: 2%; /* gapが余白を作っている可能性があるので確認 */

  height: ${(props) => props.height || 'auto'};
  width: 100%;
  max-width: 1000px; /* 最大幅を設定 */
  writing-mode: horizontal-tb; /* 横書きに設定 */
  text-orientation: mixed; /* 通常の文字方向に設定 */
  margin: 0 auto;
  margin-bottom: 2%; /* 親要素の幅に対する割合で設定 */
`;
