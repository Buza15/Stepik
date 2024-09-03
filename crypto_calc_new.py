import requests

def get_crypto_price(ticker):
    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': ticker.lower(),
        'vs_currencies': 'usd'
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raises an exception for HTTP errors
        data = response.json()
        
        if ticker.lower() in data:
            price = data[ticker.lower()]['usd']
            return f"The current price of {ticker.upper()} is ${price:.2f} USD"
        else:
            return f"Ticker '{ticker.upper()}' not found."
    
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except Exception as err:
        return f"An error occurred: {err}"

# Example usage:
ticker = input("Enter the cryptocurrency ticker symbol: ")
print(get_crypto_price(ticker))
