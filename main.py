
from crypto_data_processing import return_trending, return_table_crypto
from coingecko_api import get_prices, get_trending

response_prices = get_prices()
response_trending = get_trending().json()


if response_prices.status_code == 200:
	print(return_trending(response_trending))
	print(return_table_crypto(response_prices))
	print("This information was obtained from an API provided by CoinGecko")

else:
	print("Don't working")
