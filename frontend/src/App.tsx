import React from 'react';
import { DesignForm } from './components/DesignForm';
import { MermaidPreview } from './components/MermaidPreview';
import { OutputDisplay } from './components/OutputDisplay';


export const App: React.FC = () => {
  return (
    <div>
      <h1>設計作成ツール</h1>
      <DesignForm onSubmit={() => {}} />
      <MermaidPreview mermaidCode={''} />
      <OutputDisplay designSummary={''} designDiagram={''} />
    </div>
  );
};
