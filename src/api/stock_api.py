import requests
import pandas as pd
import os
from datetime import datetime, timedelta
import json
# Your FinHub API key
finhub_api_key = os.environ.get('FINHUB_API_KEY')

import finnhub
import pandas as pd
import os
import time

import finnhub

# Setup client
finnhub_client = finnhub.Client(api_key=finhub_api_key)

# Basic financials
#print(finnhub_client.company_basic_financials('AAPL', 'all'))

symbol = 'AAPL'

# Define the timeframe for which you want financial data (e.g., last 30 days)
end_date = datetime.now()
start_date = end_date - timedelta(days=30)

# Format dates as UNIX timestamps
start_timestamp = int(start_date.timestamp())
end_timestamp = int(end_date.timestamp())

# Fetch basic financials data using the FinHub client
response = finnhub_client.company_basic_financials(symbol, 'all')

# Ensure the 'raws' directory exists
os.makedirs('raws', exist_ok=True)

# Save the raw JSON data to a file in the 'raws' directory
json_filename = os.path.join('raws', 'financial_data.json')
with open(json_filename, 'w') as json_file:
    json.dump(response, json_file, indent=4)

print(f"Financial data saved successfully as '{json_filename}'.")