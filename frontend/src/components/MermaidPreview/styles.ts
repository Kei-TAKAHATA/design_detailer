import styled from "styled-components";
import { Button } from "../common/Button";

export const MermaidPreviewContainer = styled.div`
  width: 100%;

  border: 1px solid #ccc;  /* 薄いグレーの1ピクセルの枠線を追加 */
  box-sizing: border-box;
  // padding: 1rem;
`;

export const CopyButtonContainer = styled(Button)`
  width: 20%;
`;
