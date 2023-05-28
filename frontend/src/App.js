import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import './App.css';
import MainPage from './pages/MainPage';
import QuestionsPage from './pages/QuestionsPage';
import ResultsPage from './pages/ResultsPage';

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <Switch>
            <Route path="/" exact component={MainPage} />
            <Route path="/questions" component={QuestionsPage} />
            <Route path="/results" component={ResultsPage} />
          </Switch>
        </header>
      </div>
    </Router>
  );
}

export default App;
