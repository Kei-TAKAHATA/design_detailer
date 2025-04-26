export interface TextAreaProps extends React.TextareaHTMLAttributes<HTMLTextAreaElement> {
  $minRows?: number;
  $maxRows?: number;
  $cols?: number;
}
