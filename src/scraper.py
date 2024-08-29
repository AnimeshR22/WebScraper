import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pyppeteer import launch
from playwright.async_api import async_playwright
from zenrows import ZenRowsClient
import asyncio
import scrapy
from scrapy_splash import SplashRequest
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

async def scrape_website(url: str, scrape_types: list[str], scraper_type: str):
    if scraper_type == 'beautifulsoup':
        return scrape_with_beautifulsoup(url, scrape_types)
    elif scraper_type == 'selenium':
        return scrape_with_selenium(url, scrape_types)
    elif scraper_type == 'pyppeteer':
        return await scrape_with_pyppeteer(url, scrape_types)
    elif scraper_type == 'playwright':
        return await scrape_with_playwright(url, scrape_types)
    elif scraper_type == 'zenrows':
        return scrape_with_zenrows(url, scrape_types)
    elif scraper_type == 'scrapy_splash':
        return await scrape_with_scrapy_splash(url, scrape_types)
    else:
        raise ValueError("Invalid scraper type")

def scrape_with_beautifulsoup(url: str, scrape_types: list[str]):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return extract_data(soup, scrape_types, url)

def scrape_with_selenium(url: str, scrape_types: list[str]):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    return extract_data(soup, scrape_types, url)

async def scrape_with_pyppeteer(url: str, scrape_types: list[str]):
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto(url)
    content = await page.content()
    soup = BeautifulSoup(content, 'html.parser')
    await browser.close()
    return extract_data(soup, scrape_types, url)

async def scrape_with_playwright(url: str, scrape_types: list[str]):
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            await page.goto(url, wait_until="networkidle")
            content = await page.content()
            soup = BeautifulSoup(content, 'html.parser')
            await browser.close()
            return extract_data(soup, scrape_types, url)
    except Exception as e:
        print(f"An error occurred while scraping {url}: {str(e)}")
        return None

def scrape_with_zenrows(url: str, scrape_types: list[str]):
    client = ZenRowsClient("your_api_key_here")
    response = client.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return extract_data(soup, scrape_types, url)

def scrape_with_scrapy_splash(url: str, scrape_types: list[str]):
    class SplashSpider(scrapy.Spider):
        name = 'splash_spider'
        start_urls = [url]

        def start_requests(self):
            for url in self.start_urls:
                yield SplashRequest(url, self.parse, args={'wait': 0.5})

        def parse(self, response):
            soup = BeautifulSoup(response.body, 'html.parser')
            text = extract_text(soup)
            images = extract_images(soup, response.url)
            return {'text': text, 'images': images}

    configure_logging()
    settings = get_project_settings()
    settings.update({
        'SPLASH_URL': 'http://localhost:8050',
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy_splash.SplashCookiesMiddleware': 723,
            'scrapy_splash.SplashMiddleware': 725,
            'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
        },
        'SPIDER_MIDDLEWARES': {
            'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
        },
        'DUPEFILTER_CLASS': 'scrapy_splash.SplashAwareDupeFilter',
    })

    runner = CrawlerRunner(settings)
    d = runner.crawl(SplashSpider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()

    # Return the items collected by the spider
    return SplashSpider.items

def extract_data(soup, scrape_types: list[str], url: str):
    result = {}
    
    if 'Text' in scrape_types:
        result['text'] = extract_text(soup)
    
    if 'Image' in scrape_types:
        result['images'] = extract_images(soup, url)
    
    return result

def extract_text(soup):
    # Extract all text from the page
    text = soup.get_text(separator='\n', strip=True)
    # Remove extra whitespace and empty lines
    text = '\n'.join(line.strip() for line in text.split('\n') if line.strip())
    return text

def extract_images(soup, url):
    images = []
    for img in soup.find_all('img'):
        src = img.get('src')
        if src:
            if src.startswith('http'):
                images.append(src)
            else:
                images.append(f"{url.rstrip('/')}/{src.lstrip('/')}")
    return images[:5]  # Limit to 5 images