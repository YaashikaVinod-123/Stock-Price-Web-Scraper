import requests
from bs4 import BeautifulSoup

# URL of the stock page on Yahoo Finance
url = 'https://finance.yahoo.com/quote/AAPL'

try:
    # Add headers to mimic a real browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    # Send an HTTP request to the website
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Check for request errors

    # Parse the content of the webpage
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the stock price using the updated element
    stock_price = soup.find('fin-streamer', {'data-field': 'regularMarketPrice'})
    
    if stock_price:
        print("Current Stock Price:", stock_price.text)
    else:
        print("Stock price not found on the page.")
except Exception as e:
    print(f"An error occurred: {e}")
