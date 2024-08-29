from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from scraper import scrape_website
from fastapi.middleware.cors import CORSMiddleware
import asyncio

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React app's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ScrapeRequest(BaseModel):
    url: str
    scrape_types: list[str]
    scraper_type: str

@app.post("/api/scrape")
async def scrape(request: ScrapeRequest):
    try:
        scraped_data = await scrape_website(request.url, request.scrape_types, request.scraper_type)
        return {"data": scraped_data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/")
async def root():
    return {"message": "Welcome to the Web Scraper API"}


if __name__ == "__main__":
    import uvicorn
    asyncio.run(uvicorn.run(app, host="0.0.0.0", port=8000))
    
    
"""
The request format for Postman should be:

Method: POST
URL: http://localhost:8000/api/scrape
Headers:
    Content-Type: application/json
Body (raw JSON):
{
    "url": "https://example.com",
    "scrape_types": ["Text", "Image", "Video"],
    "scraper_type": "beautifulsoup"
}

Note: 
- 'url' should be the website you want to scrape
- 'scrape_types' can include any combination of "Text", "Image", and "Video"
- 'scraper_type' can be "beautifulsoup", "selenium", or "pyppeteer"
"""
    