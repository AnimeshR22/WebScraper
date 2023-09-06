from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import requests
import time

# Create a WebDriver instance (for Chrome)
driver = webdriver.Chrome()

url = 'https://www.google.com/search?sca_esv=563100770&rlz=1C1CHBF_enIN1052IN1052&sxsrf=AB5stBhGjS5QeJ67IIQXQeoFSahArV2R0g:1694018111554&q=idli&tbm=isch&source=lnms&sa=X&ved=2ahUKEwjfvaCetZaBAxWpbmwGHbWQDLUQ0pQJegQICRAB&biw=1920&bih=955&dpr=1'
driver.get(url)

# Function to scroll down the page until no more images are loaded
def scroll_to_bottom(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Adjust the sleep duration as needed
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

# Scroll down to load more images
scroll_to_bottom(driver)

# Find all image elements on the page
image_elements = driver.find_elements(By.TAG_NAME, 'img')

# Extract image URLs from the 'src' attribute, filter out invalid URLs
image_urls = [img.get_attribute('src') for img in image_elements if img.get_attribute('src') and img.get_attribute('src').startswith('http')]

# Create a directory for image downloads
image_directory = 'images'
os.makedirs(image_directory, exist_ok=True)

for i, img_url in enumerate(image_urls):
    try:
        img_response = requests.get(img_url)
        if img_response.status_code == 200:
            img_filename = os.path.join(image_directory, f'image_{i}.jpg')
            with open(img_filename, 'wb') as img_file:
                img_file.write(img_response.content)
            print(f"Image downloaded: {img_filename}")
    except Exception as e:
        print(f"Error downloading image: {str(e)}")

driver.quit()
