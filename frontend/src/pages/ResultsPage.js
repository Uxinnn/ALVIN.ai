// ResultsPage.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useHistory } from 'react-router-dom';
import StatsDisplay from './StatsDisplay';

function ResultsPage() {
  const [summaryStats, setSummaryStats] = useState({
    easy: { answered: 0, correct: 0 },
    medium: { answered: 0, correct: 0 },
    hard: { answered: 0, correct: 0 },
  });
  const history = useHistory();

  useEffect(() => {
    // fetch data from the backend
    axios.get('/api/summaryStats')
      .then(response => {
        // use real data if it's available
        if (response.data) {
          setSummaryStats(response.data);
        }
      });
  }, []);

  // Calculate accuracies
  const accuracies = {
    easy: summaryStats.easy.answered > 0 ? (summaryStats.easy.correct / summaryStats.easy.answered * 100).toFixed(2) : 0,
    medium: summaryStats.medium.answered > 0 ? (summaryStats.medium.correct / summaryStats.medium.answered * 100).toFixed(2) : 0,
    hard: summaryStats.hard.answered > 0 ? (summaryStats.hard.correct / summaryStats.hard.answered * 100).toFixed(2) : 0,
  }

  return (
    <div className="ResultsPage">
      <h1>Results</h1>
      <StatsDisplay stats={summaryStats} accuracies={accuracies} />
      <button onClick={() => history.push('/')}>Return Home</button>
    </div>
  );
}

export default ResultsPage;
