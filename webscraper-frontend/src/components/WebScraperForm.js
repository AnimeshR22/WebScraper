import React, { useState } from 'react';

function WebScraperForm() {
    const [url, setUrl] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const [isProgressing, setIsProgressing] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setIsProgressing(true);
        setIsLoading(true);
        try {
            const response = await fetch('/api/scrape', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ url }),
            });
            const data = await response.json();
            // Handle the scraped data here
            console.log(data);
        } catch (error) {
            console.error('Error scraping data:', error);
        }
        setIsLoading(false);
        setIsProgressing(false);
    };

    return (
      <section className="w-full h-full bg-black py-12 md:py-24 lg:py-32 xl:py-48">
        <div className="container mx-auto px-4 h-full flex items-center justify-center py-8">
          <div className="w-full max-w-4xl">
            <div className="flex flex-col justify-center space-y-8 text-center ">
             <div className="space-y-2 -mt-4 py-4">
              <h1 className="text-3xl font-bold tracking-tighter sm:text-5xl xl:text-6xl/none">
                <span className="bg-clip-text text-transparent bg-gradient-to-r from-green-500 via-yellow-500 to-red-500 animate-gradient-x">Discover </span>{" "}
                <span className="bg-clip-text text-transparent bg-gradient-to-r from-white via-silver-500 to-gray-500 animate-gradient-x">Scraping</span>
              </h1>
              <p className="max-w-[600px] text-zinc-200 md:text-xl dark:text-zinc-400 mx-auto ">
                Scrap Like nothing Before
              </p>
            </div>
            <form onSubmit={handleSubmit} className="flex flex-col items-center space-y-4 w-full">
              <div className="relative w-full max-w-2xl glow-effect">
                <input
                  type="text"
                  value={url}
                  onChange={(e) => setUrl(e.target.value)}
                  placeholder="Enter URL to scrape"
                  className="w-full px-4 py-2 pr-12 rounded-lg bg-zinc-800 text-white placeholder-zinc-400 focus:outline-none text-base font-sans relative z-10"
                />
                <div className="glow-container">
                  <div className="glow"></div>
                </div>
                <button
                  type="submit"
                  disabled={isLoading}
                  className="absolute right-2 top-1/2 transform -translate-y-1/2 px-3 py-1 bg-zinc-700 text-white rounded-lg hover:bg-zinc-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 focus:ring-offset-zinc-800 transition-all duration-200 ease-in-out"
                >
                  {isLoading ? (
                    <span className="flex items-center">
                      <svg className="animate-spin -ml-1 mr-2 h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                        <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                        <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                      </svg>
                      Scraping...
                    </span>
                  ) : (
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M14 5l7 7m0 0l-7 7m7-7H3" />
                    </svg>
                  )}
                </button>
              </div>
            </form>
          </div>
        </div>
        </div>
      </section>
    )
}

export default WebScraperForm;
