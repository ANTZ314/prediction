# -*- coding: utf-8 -*-
"""
Description:
* URL request data retrieval from alpha-vantage
* Key: PBRGXKAUD9LKYI3Z

Note: 
Run in 'crypto' virtual environment


Use:
python3 api3.py
"""
import json
import requests
import alpha_vantage
from pprint import pprint

def main():
	API_URL = "https://www.alphavantage.co/query" 
	#symbols = ['QCOM',"INTC","PDD"]
	#symbols = ['QCOM',"TSLA","MSFT"]
	symbols = ['QCOM']
	open1 = 0.1

	for symbol in symbols:
		data = { "function": "TIME_SERIES_INTRADAY", "symbol": symbol,"interval" : "60min","datatype": "json","apikey": "PBRGXKAUD9LKYI3Z" } 

		#print('s')
		response = requests.get(API_URL, data)
		data = response.json()
		print(symbol)
		a = (data['Time Series (60min)'])
		keys = (a.keys())

		try:

			## NOTE: Either print the entire fucking list or just the date?

			#print('OPEN\tCLOSE')
			#for key in keys:
			#	print(a[key]['1. open'] + " " + a[key]['4. close'])

			## Only printing the the first column: DATE????
			print(list(a.keys())[10])
			print(list(keys)[2])

			## How the fuck do you print the next column: OPEN????

		except:
			print('Failed...')

if __name__ == "__main__": main()