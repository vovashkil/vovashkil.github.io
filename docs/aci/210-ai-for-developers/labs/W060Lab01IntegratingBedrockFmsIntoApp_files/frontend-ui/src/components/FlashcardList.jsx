// FlashcardList.js
import React from 'react';
import Flashcard from './Flashcard';
import './Flashcard.css';



const FlashcardList = ({flashcards}) => {
  return (
    <div className="flashcard-list">
      {flashcards.map((card, index) => (
        <Flashcard key={index} front={card.front} back={card.back} />
      ))}
    </div>
  );
};

export default FlashcardList;
