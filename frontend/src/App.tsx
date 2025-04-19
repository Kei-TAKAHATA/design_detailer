import React from 'react';
import DesignForm from './components/DesignForm';
import MermaidPreview from './components/MermaidPreview';
import OutputDisplay from './components/OutputDisplay';

const App: React.FC = () => {
  return (
    <div>
      <h1>Design Detailer App</h1>
      <DesignForm />
      <MermaidPreview />
      <OutputDisplay />
    </div>
  );
};

export default App;