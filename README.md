# Bitcoin Price Tracker

A simple Python script that fetches the current Bitcoin price and 24-hour price change using the CoinGecko API.

## Features

- Real-time Bitcoin price updates
- 24-hour price change percentage
- Automatic updates every 60 seconds
- Error handling for API requests

## Requirements

- Python 3.6 or higher
- `requests` library

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/jakedh123/btc_price.git
   cd btc_price
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script using Python:

```bash
python btc_price.py
```

The script will continuously fetch and display the Bitcoin price every 60 seconds. Press Ctrl+C to stop the script.

## Sample Output

```
Starting Bitcoin Price Tracker...
Press Ctrl+C to exit

Timestamp: 2025-01-07 03:31:26
Bitcoin Price: $45,123.45
24h Change: 2.34%
```

## API Reference

This project uses the [CoinGecko API](https://www.coingecko.com/en/api) to fetch Bitcoin price data. The API is free to use and doesn't require authentication for basic endpoints.

## License

MIT