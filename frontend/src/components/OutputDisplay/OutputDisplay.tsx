import React from 'react';
import { OutputDisplayProps } from './types';

export const OutputDisplay: React.FC<OutputDisplayProps> = ({ designSummary, designDiagram }) => {
  return (
    <div>
      <h2>Output Display</h2>
      <div id="design-summary"></div>
      <div id="design-diagram"></div>
    </div>
  );
};
