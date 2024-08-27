from flask import Flask, jsonify, request, render_template
from scraper import scrape_website
import os
app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.json
    url = data.get('url', 'https://example.com')
    scraped_data = scrape_website(url)
    return jsonify({"data": scraped_data})

if __name__ == '__main__':
    app.run(debug=True)