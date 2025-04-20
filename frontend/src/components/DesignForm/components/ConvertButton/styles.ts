import styled from 'styled-components';

// export const ButtonContainer = styled.button`
//   background-color: #007bff;
//   color: #fff;
//   padding: 10px 20px;
//   border: none;
//   border-radius: 5px;
//   cursor: pointer;
//   &:hover {
//     background-color: #0056b3;
//   }
// `;

export const StyledConvertButton = styled.button`
  height: 100%; /* 親要素の高さに合わせる */
  width: 20%;
  padding: 0.5rem 4rem; /* ボタンの内側の余白を設定 */
  margin-left: auto; /* 右揃えにするための設定 */

  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;

  &:hover {
    background-color: #0056b3;
  }
`;
