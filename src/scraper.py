from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def scrape_website(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    
    driver.get(url)
    
    # Wait for the page to load
    time.sleep(2)
    
    # Example: scrape all paragraph text
    paragraphs = driver.find_elements(By.TAG_NAME, 'p')
    scraped_data = [p.text for p in paragraphs]
    
    driver.quit()
    
    return scraped_data