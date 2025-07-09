import React from 'react';
import './QuoteCard.css';

const QuoteCard = ({ quote, onFavorite, onShare, isFavorite }) => {
  return (
    <div className="quote-card">
      <p className="quote-text">“{quote.text}”</p>
      <p className="quote-author">– {quote.author}</p>
      <div className="actions">
        <button onClick={onShare}>Share</button>
        <button onClick={onFavorite}>
          {isFavorite ? '★ Favorited' : '☆ Favorite'}
        </button>
      </div>
    </div>
  );
};

export default QuoteCard;