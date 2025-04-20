import React from 'react';
import { DesignForm } from './components/DesignForm';
import { MermaidPreview } from './components/MermaidPreview';
import { OutputDisplay } from './components/OutputDisplay';


export const App: React.FC = () => {

  return (
    <div>
      <h2>設計を作成するツールだよー</h2>
      <DesignForm onSubmit={() => {}} />
      <MermaidPreview mermaidCode={''} />
      <OutputDisplay designSummary={''} designDiagram={''} />
    </div>
  );
};
