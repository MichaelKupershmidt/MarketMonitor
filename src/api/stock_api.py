import requests
import pandas as pd
import os
from datetime import datetime, timedelta
import json
import finnhub
import requests
from bs4 import BeautifulSoup

def get_sp500_tickers():
    sp500_url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    response = requests.get(sp500_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'id': 'constituents'})
    
    # Parse the table
    df = pd.read_html(str(table))[0]
    sp500_tickers = df['Symbol'].tolist()
    
    return sp500_tickers
# Setup client
finnhub_client = finnhub.Client(api_key='c7f78v2ad3ib5ruekktg')

def get_company_profile(ticker):
    response = finnhub_client.company_profile2(symbol=ticker)
    return response

def get_company_metrics(ticker):
    response = finnhub_client.company_basic_financials(ticker, 'all')
    return response['metric']
