import requests
import time
from datetime import datetime

def get_bitcoin_price():
    """Fetch current Bitcoin price from CoinGecko API"""
    try:
        # CoinGecko API endpoint for Bitcoin price in USD
        url = 'https://api.coingecko.com/api/v3/simple/price'
        params = {
            'ids': 'bitcoin',
            'vs_currencies': 'usd',
            'include_24hr_change': 'true'
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        data = response.json()
        price = data['bitcoin']['usd']
        price_change = data['bitcoin']['usd_24h_change']
        
        return {
            'price': price,
            'price_change_24h': price_change,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
    except requests.exceptions.RequestException as e:
        print(f'Error fetching Bitcoin price: {e}')
        return None

def main():
    while True:
        price_data = get_bitcoin_price()
        if price_data:
            print(f"\nTimestamp: {price_data['timestamp']}")
            print(f"Bitcoin Price: ${price_data['price']:,.2f}")
            print(f"24h Change: {price_data['price_change_24h']:.2f}%")
        
        # Wait for 60 seconds before the next update
        time.sleep(60)

if __name__ == '__main__':
    print('Starting Bitcoin Price Tracker...')
    print('Press Ctrl+C to exit')
    try:
        main()
    except KeyboardInterrupt:
        print('\nBitcoin Price Tracker stopped.')