import styled from "styled-components";
import { Button } from "../common/Button";

export const DesignDetailEditorContainer = styled.div`
  display: flex;
  flex-direction: row; /* 子要素を横に並べる */
  gap: 2%; /* 子要素間の隙間を設定 */
  width: 100%;
  margin-bottom: 2%; /* 親要素の幅に対する割合で設定 */
`;

export const UpdateButtonContainer = styled(Button)`
  width: 20%;
  padding: 0.5rem 4rem; /* ボタンの内側の余白を設定 */
  margin-left: auto; /* 右揃えにするための設定 */
`;
