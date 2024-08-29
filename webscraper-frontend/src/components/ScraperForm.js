import React, { useState } from 'react';
import './ScraperForm.css';

const ScraperForm = () => {
    const [url, setUrl] = useState('');
    const [scrapeTypes, setScrapeTypes] = useState([]);
    const [scraperType, setScraperType] = useState('beautifulsoup');
    const [scrapedData, setScrapedData] = useState(null);
    const [isLoading, setIsLoading] = useState(false);

    const handleScrapeTypeChange = (type) => {
        if (scrapeTypes.includes(type)) {
            setScrapeTypes(scrapeTypes.filter(t => t !== type));
        } else {
            setScrapeTypes([...scrapeTypes, type]);
        }
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setIsLoading(true);
        try {
            const response = await fetch('/api/scrape', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ url, scrape_types: scrapeTypes, scraper_type: scraperType }),
            });
            const data = await response.json();
            setScrapedData(data.data);
        } catch (error) {
            console.error('Error scraping data:', error);
        }
        setIsLoading(false);
    };

    return (
        <div className="scraper-container">
            <h1>Web Scraper</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={url}
                    onChange={(e) => setUrl(e.target.value)}
                    placeholder="Enter URL to scrape"
                />
                <div className="scrape-options">
                    <button
                        type="button"
                        onClick={() => handleScrapeTypeChange('Text')}
                        className={scrapeTypes.includes('Text') ? 'active' : ''}
                    >
                        Text
                    </button>
                    <button
                        type="button"
                        onClick={() => handleScrapeTypeChange('Image')}
                        className={scrapeTypes.includes('Image') ? 'active' : ''}
                    >
                        Image
                    </button>
                </div>
                <div className="scraper-type">
                    <label htmlFor="scraper-select">Choose a scraper:</label>
                    <select
                        id="scraper-select"
                        value={scraperType}
                        onChange={(e) => setScraperType(e.target.value)}
                    >
                        <option value="beautifulsoup">BeautifulSoup</option>
                        <option value="selenium">Selenium</option>
                        <option value="pyppeteer">Pyppeteer</option>
                        <option value="playwright">Playwright</option>
                        {/* <option value="zenrows">ZenRows</option> */}
                        <option value="scrapy_splash">Scrapy Splash</option>
                    </select>
                </div>
                <button type="submit" disabled={isLoading || scrapeTypes.length === 0}>
                    {isLoading ? 'Scraping...' : 'Scrape'}
                </button>
            </form>
            {scrapedData && (
                <div className="scraped-data">
                    <h2>Scraped Data:</h2>
                    {scrapedData.text && (
                        <div>
                            <h3>Text:</h3>
                            <pre>{scrapedData.text}</pre>
                        </div>
                    )}
                    {scrapedData.images && (
                        <div>
                            <h3>Images:</h3>
                            {scrapedData.images.map((src, index) => (
                                <img key={index} src={src} alt={`Scraped ${index}`} />
                            ))}
                        </div>
                    )}
                </div>
            )}
        </div>
    );
};

export default ScraperForm;
