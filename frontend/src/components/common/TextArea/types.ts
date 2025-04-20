export type TextAreaProps = {
  value: string;
  onChange: (event: React.ChangeEvent<HTMLTextAreaElement>) => void;
  $minRows?: number;
  $maxRows?: number;
  $cols?: number;
  placeholder?: string;
};
