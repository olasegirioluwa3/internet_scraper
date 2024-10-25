from flask import Flask, jsonify, request
from zr_google_scraper import GoogleScraper
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Accessing the environment variable
proxy_http = os.getenv('PROXY_URI_HTTP')

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def scrape():
    name = request.args.get('name')
    proxies = {
        "http": proxy_http
    }
    
    if not name:
        return jsonify({"error": "Missing 'name' parameter"}), 400
    
    try:
        # Initialize the scraper class with proxies
        scraper = GoogleScraper(proxies=proxies)
        # Use the 'scrape' method of the class
        scraped_data = scraper.scrape(name)
        return jsonify({"data": scraped_data})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
