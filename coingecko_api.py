import requests

api_get_prices = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum%2Cbinancecoin%2Ccardano%2C&vs_currencies=usd"
api_get_trending = "https://api.coingecko.com/api/v3/search/trending"

def get_prices():
	return requests.get(api_get_prices)

def get_trending():
	return requests.get(api_get_trending)