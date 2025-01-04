import requests

from rich.console import Console
from rich.table import Table
from rich.box import SQUARE_DOUBLE_HEAD

console = Console()

cryptos = 'BTC,ETH,BNB,USDT,ADA,SOL,XRP,DOT,DOGE,SHIB,LTC,LINK,MATIC,XLM,TRX,AVAX,ATOM,DASH,XMR,BCH'
currencies = 'BTC,USD,EUR,INR'
key = '75e8d2935dd437dcdc0bb7ce99136a01086bd8e00e040e63d1ccc6192679b09d'

url = f'https://min-api.cryptocompare.com/data/pricemulti?fsyms={cryptos}&tsyms={currencies}&api_key={key}'

def crypto_data():
  response = requests.get(url)
  if (response.status_code == 200):
    try:
      return response.json()
    except ValueError:
      print('Invalid JSON response from the API.')
  else:
    print('Failed to fetch the crypto data.')

data = crypto_data()

def display_crypto(data):
  table = Table(title='CryptoCurrency Prices', style='cyan', border_style='green', box=SQUARE_DOUBLE_HEAD)
  table.add_column("CryptoCurrency", min_width=20, style="white", justify="center")
  table.add_column("Bitcons (BTC)", max_width=15, style="bold green", justify="left")
  table.add_column("Dollars (USD)", max_width=15, style="white", justify="right")
  table.add_column("Euros (EUR)", max_width=15, style="bold green", justify="left")
  table.add_column("Rupees (INR)", max_width=15, style="white", justify="right")
  for coin, prices in data.items():
    table.add_row(coin, str(prices['BTC']),str(prices['USD']),str(prices['EUR']),str(prices['INR']))
  console.print(table)
    

display_crypto(data)

