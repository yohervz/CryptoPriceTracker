from prettytable import PrettyTable

def parse_and_sort_json_file(response):
	cryptos_json = response.json()
	crypto_prices = sorted(cryptos_json.items(), key=lambda x: x[1]["usd"], reverse=True)
	return crypto_prices

def parse_json_trending(response):
	result = []
	for i in range(4):
	    coin = response['coins'][i]
	    result.append((coin['item']['name']))
	return result
	

def return_trending(response, tablesTrending="Trending: "):

	cryptos = parse_json_trending(response)

	for i in range(len(cryptos)):
		tablesTrending += f"| {cryptos[i].capitalize()} "
	
	tablesTrending += "|"
	return tablesTrending

def return_table_crypto(response):
	table = PrettyTable()
	table.field_names = ["Crypto", "Prices (USD)"]
	table.align = "l"
	crypto_prices = parse_and_sort_json_file(response)

	for i in range(len(crypto_prices)):
		table.add_row([crypto_prices[i][0].capitalize(), crypto_prices[i][1]["usd"]])
	return table
