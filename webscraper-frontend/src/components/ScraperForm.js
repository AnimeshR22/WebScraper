import React, { useState } from 'react';
import './ScraperForm.css';

const ScraperForm = () => {
  const [url, setUrl] = useState('');
  const [scrapeType, setScrapeType] = useState([]);

  const handleScrapeTypeChange = (type) => {
    if (scrapeType.includes(type)) {
      setScrapeType(scrapeType.filter(t => t !== type));
    } else {
      setScrapeType([...scrapeType, type]);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('URL:', url, 'Scrape Types:', scrapeType);
    // Implement scraping logic here
  };

  return (
    <div className="scraper-container">
      <h1>SCRAPE</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="Enter the URL of the website you wish to scrape"
        />
        <div className="scrape-options">
          <p>select:</p>
          <div className="button-group">
            {['Text', 'Image', 'Video'].map((type) => (
              <button
                key={type}
                type="button"
                className={scrapeType.includes(type) ? 'active' : ''}
                onClick={() => handleScrapeTypeChange(type)}
              >
                {type}
              </button>
            ))}
          </div>
        </div>
        <button type="submit" className="download-button">
          Download
        </button>
      </form>
    </div>
  );
};

export default ScraperForm;
