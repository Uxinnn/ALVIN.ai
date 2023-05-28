// StatsDisplay.js
import React from 'react';

function Stats({ stats, accuracies }) {
  return (
    <div className="SummaryStats">
      <h2>Summary Stats</h2>
     
      {Object.entries(stats).map(([key, value]) => (
        <div key={key}>
          <p>{key.toUpperCase()} QUESTIONS</p>
          <p>Answered: {value.answered}</p>
          <p>Correct: {value.correct}</p>
          <p>Accuracy: {accuracies[key]}%</p>
        </div>
      ))}
    </div>
  );
}

export default Stats;
