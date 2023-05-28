import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Modal from 'react-modal';
import { useHistory } from 'react-router-dom';

Modal.setAppElement('#root'); // Required for accessibility purposes

function QuestionsPage() {
  const [currentQuestion, setCurrentQuestion] = useState(null);
  const [userResponse, setUserResponse] = useState("");
  const [isCorrect, setIsCorrect] = useState(null);
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const history = useHistory();

  useEffect(() => {
    // Fetch the first question when the page loads
    axios.get('/api/questions')
      .then(response => {
        setCurrentQuestion(response.data);
      });
  }, []);

  function handleUserResponse() {
    // Send the user's response to the backend
    axios.post('/api/answers', { question: currentQuestion, answer: userResponse })
      .then(response => {
        // The backend should return whether the answer was correct and the next question
        setIsCorrect(response.data.isCorrect);
        setCurrentQuestion(response.data.nextQuestion);
        setModalIsOpen(true);
      });
  }

  function closeModal() {
    setModalIsOpen(false);
    setUserResponse("");
  }

  function endTest() {
    history.push('/results');
  }

  return (
    <div className="QuestionsPage">
      <h1>Questions</h1>
      <button onClick={endTest} className="end-button">End</button>
      {currentQuestion && (
        <div>
          <p>{currentQuestion}</p>
          <input value={userResponse} onChange={e => setUserResponse(e.target.value)} />
          <button onClick={handleUserResponse}>Submit</button>
        </div>
      )}
      <Modal
        isOpen={modalIsOpen}
        onRequestClose={closeModal}
        contentLabel="Answer Feedback Modal"
      >
        <h2>{isCorrect ? 'Correct!' : 'Incorrect'}</h2>
        <button onClick={closeModal}>OK</button>
      </Modal>
    </div>
  );
}

export default QuestionsPage;
