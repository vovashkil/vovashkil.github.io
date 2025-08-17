// App.js
import React, { useState } from 'react';
import Form from './components/Form';
import FlashcardList from './components/FlashcardList';
import './App.css';

const App = () => {
  const [flashcards, setFlashcards] = useState([]);

  return (
    <div className="app">
      <h1>Flashcards</h1>
      <Form setFlashcards={setFlashcards} />
      <FlashcardList flashcards={flashcards} />
    </div>
  );
};

export default App;