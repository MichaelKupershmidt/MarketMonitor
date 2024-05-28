import requests
import pandas as pd
import os


# Your Alpha Vantage API key
api_key = os.environ.get('MY_API_KEY')

# Function to get stock data from Alpha Vantage
def get_stock_data(symbol='IBM', interval='1min'):
    url = f'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': interval,
        'apikey': api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

# Function to save data in JSON format
def save_as_json(data, filename):
    with open(filename, 'w') as f:
        pd.DataFrame(data).to_json(f, orient='records', lines=True)

# Function to save data in CSV format
def save_as_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

# Function to save data in Excel format
def save_as_excel(data, filename):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)

# Example usage
symbol = 'AAPL'
data = get_stock_data(symbol)

# Save data in different formats
save_as_json(data, 'raws/stock_data.json')
save_as_csv(data, 'raws/stock_data.csv')
save_as_excel(data, 'raws/stock_data.xlsx')

print("Data saved successfully!")
