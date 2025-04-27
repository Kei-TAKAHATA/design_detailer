import styled from 'styled-components';
import { TextAreaProps } from './types';

export const TextAreaContainer = styled.textarea<TextAreaProps>`
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
`;
