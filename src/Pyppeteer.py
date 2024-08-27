import asyncio
import os
import requests
from pyppeteer import launch
from pyppeteer.errors import TimeoutError, PageError, NetworkError

async def main():
    # Launch headless Chromium browser
    browser = await launch(headless=False)
    
    try:
        # Create a new page
        page = await browser.newPage()
        
        # Set the URL to scrape
        url = 'https://www.google.co.in/search?sca_esv=d71f265c45fd02a5&sca_upv=1&sxsrf=ADLYWIIknZLex4lhtewydM90vNgx1jwW8g:1724699900521&q=banana+image&udm=2&fbs=AEQNm0CvspUPonaF8UH5s_LBD3JPX4RSeMPt9v8oIaeGMh2T2D1DyqhnuPxLgMgOaYPYX7OtOF4SxbM4YPsyWUMdeXRPnkQc3caC_NEMjyGZlBqX7YDVSc-lk14rE2h7j-ln6ORWjT4WxqVC6FS82YpEwEqqnkJJKpHqKGrk5ZhbNsOcE3i19GRoFANVfwr_gZS3oWcL17KMyupN4i8_p5OTUvqC1CSN_g&sa=X&ved=2ahUKEwi3rqjnr5OIAxW2s1YBHRW3O24QtKgLegQIFhAB&biw=1865&bih=924&dpr=1'  # Replace with your desired URL
        await page.goto(url, {'waitUntil': 'domcontentloaded'})

        # Extract text from the page
        text_content = await page.evaluate('''() => {
            return document.body.textContent;
        }''')

        # Save text content to a text file
        text_filename = 'text_content.txt'
        with open(text_filename, 'w', encoding='utf-8') as text_file:
            text_file.write(text_content)

        print(f"Text Content saved to: {text_filename}")
       
        # Download and save images continuously
        await download_images(page)

    except (TimeoutError, PageError) as e:
        print(f"An error occurred: {str(e)}")

    finally:
        # Close the browser
        await browser.close()

async def download_images(page):
    # Create a directory for image downloads
    image_directory = 'test_images'
    os.makedirs(image_directory, exist_ok=True)

    while True:
        try:
            # Extract images from the current page
            image_urls = await page.evaluate('''() => {
                const images = Array.from(document.querySelectorAll('img'));
                return images.map(img => img.src);
            }''')

            # Download and save images one by one
            for i, img_url in enumerate(image_urls):
                img_response = requests.get(img_url)
                if img_response.status_code == 200:
                    img_filename = os.path.join(image_directory, f'image_{i}.jpg')
                    with open(img_filename, 'wb') as img_file:
                        img_file.write(img_response.content)
                    print(f"Image downloaded: {img_filename}")

            # Click the "Load More" button to load additional images
            load_more_button_selector = 'selector_for_load_more_button'  # Replace with the actual selector
            await page.click(load_more_button_selector)

            # Delay to allow new images to load
            await asyncio.sleep(2)

        except NetworkError:
            # Handle the network error (context destroyed) and continue
            print("NetworkError - Handling and continuing...")
            continue

        # Check if there are no more images to load
        no_more_images = await page.evaluate('''() => {
            const images = Array.from(document.querySelectorAll('img'));
            return images.length === 0;
        }''')

        if no_more_images:
            break

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
