import requests
import json

def getData(ticker):
	url = 'https://api.iextrading.com/1.0/stock/' + ticker + '/chart/1m'
	r = requests.get(url)
	raw = json.loads(r.text)
	print(r.text)

	temp = []
	for element in raw:
		temp.append(element["open"])

	print(temp)

if __name__ == '__main__':
    getData("aapl")