export type DesignDetailEditorProps = {
  onSubmit: () => void;
  designDetailText: string;
  onChange: (event: React.ChangeEvent<HTMLTextAreaElement>) => void;
};