import React, { useEffect, useState } from 'react';
import quotes from './data/quotes';
import QuoteCard from './components/QuoteCard';
import './App.css';

function App() {
  const [currentQuote, setCurrentQuote] = useState(null);
  const [favorites, setFavorites] = useState([]);

  useEffect(() => {
    const savedFavorites = JSON.parse(localStorage.getItem('favorites')) || [];
    setFavorites(savedFavorites);
    loadDailyQuote();
  }, []);

  const loadDailyQuote = () => {
    const today = new Date().toDateString();
    const storedDate = localStorage.getItem('quoteDate');
    let quote;

    if (storedDate === today) {
      quote = JSON.parse(localStorage.getItem('quoteOfTheDay'));
    } else {
      quote = quotes[Math.floor(Math.random() * quotes.length)];
      localStorage.setItem('quoteOfTheDay', JSON.stringify(quote));
      localStorage.setItem('quoteDate', today);
    }

    setCurrentQuote(quote);
  };

  const toggleFavorite = () => {
    const isFav = favorites.some(f => f.text === currentQuote.text);
    let updatedFavorites;

    if (isFav) {
      updatedFavorites = favorites.filter(f => f.text !== currentQuote.text);
    } else {
      updatedFavorites = [...favorites, currentQuote];
    }

    setFavorites(updatedFavorites);
    localStorage.setItem('favorites', JSON.stringify(updatedFavorites));
  };

  const shareQuote = () => {
    const message = `“${currentQuote.text}” – ${currentQuote.author}`;
    navigator.clipboard.writeText(message);
    alert('Quote copied to clipboard!');
  };

  const isFavorite = favorites.some(f => f.text === currentQuote?.text);

  return (
    <div className="App">
      <h1>🌟 Quote of the Day</h1>
      {currentQuote && (
        <QuoteCard
          quote={currentQuote}
          onFavorite={toggleFavorite}
          onShare={shareQuote}
          isFavorite={isFavorite}
        />
      )}

      {favorites.length > 0 && (
        <div className="favorites">
          <h2>⭐ Your Favorites</h2>
          {favorites.map((q, i) => (
            <p key={i}>“{q.text}” – {q.author}</p>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;