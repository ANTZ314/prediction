# -*- coding: utf-8 -*-
"""
Description:
* URL request data retrieval from alpha-vantage 
* Extracts the opening price and converts from pandas to float value
* plots closing values on graph
* Key: PBRGXKAUD9LKYI3Z

Note: 
Run in 'crypto' virtual environment

Use:
python3 api3.py
"""
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
from pprint import pprint

def main():
	ticker = 'MSFT'
	tail = 'string'		# string
	open1 = 0.1			# float
	close1 = 0.1		# float
	high1 = 0.1			# float
	low1 = 0.1			# float

	ts = TimeSeries(key='PBRGXKAUD9LKYI3Z', output_format='pandas')
	data, meta_data = ts.get_intraday(symbol=ticker,interval='1min', outputsize='full')
	print('\nTicker: ' + ticker)
	#pprint(data.tail(3))

	try:
		tail = data.tail(1)						# get last line of json data
		open1 = tail['1. open']					# pandas float with index
		open1 = float(open1)					# convert to float for calculations

		close1 = tail['4. close']				# pandas float with index
		close1 = float(close1)					# convert to float for calculations

		#tail = open1.to_string(index=False)	# 'tail'  (string) used for storage

		#print('closes: ' + str(open1))			# prints with pandas index shit
		#print(open1.to_string(index=False))	# get rid of panda index data
		print("Open stock price: " + str(open1))
		print("Close stock price: " + str(close1))
	except:
		print('Failed...')

	data['4. close'].plot()
	plt.title('Intraday Times Series for the MSFT stock (1 min)')
	plt.show()
	print('Complete...')

if __name__ == "__main__": main()