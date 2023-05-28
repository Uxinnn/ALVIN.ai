import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Stats from '../components/Stats';

function MainPage() {
  const [summaryStats, setSummaryStats] = useState({
    easy: { answered: 0, correct: 0 },
    medium: { answered: 0, correct: 0 },
    hard: { answered: 0, correct: 0 },
  });
  const [projectedAbilities, setProjectedAbilities] = useState("Thinker");

  useEffect(() => {

    axios.get('/api/summaryStats')
      .then(response => {
       
        if (response.data) {
          setSummaryStats(response.data);
        }
      });

    axios.get('/api/projectedAbilities')
      .then(response => {
       
        if (response.data) {
          setProjectedAbilities(response.data);
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
    <div className="MainPage">
      <h1>Main Page</h1>
      <Stats stats={summaryStats} accuracies={accuracies} />
      <div className="ProjectedAbilities">
        <h2>Projected Abilities</h2>
        
        <p>The student is a(n): {projectedAbilities}</p>
      </div>
    </div>
  );
}

export default MainPage;
