import styled from "styled-components";
import { Button } from "../common/Button";

export const StyledMermaidPreview = styled.div`
  width: 100%;
  max-width: 1000px; /* 最大幅を設定 */

  border: 1px solid #ccc;  /* 薄いグレーの1ピクセルの枠線を追加 */
  box-sizing: border-box;
  // padding: 1rem;
`;

export const StyledCopyButton = styled(Button)`
  width: 20%;
  max-width: 1000px; /* 最大幅を設定 */
`;