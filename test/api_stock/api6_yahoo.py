# -*- coding: utf-8 -*-
"""
Description:
Using "yahoo_fin" package to fetch the live stock price of provided TICKER code
Can also fetch historical data witihin specified date range (start - end)
Then extract the Opening price but...
-> can't seem to fetch todays date (error after 2 days ago)

Note: 
* Run in 'crypto' virtual environment  
* http://theautomatic.net/yahoo_fin-documentation/
* http://theautomatic.net/2018/07/31/how-to-get-live-stock-prices-with-python/

Dependencies:
sudo pip install yahoo_fin
sudo pip install --upgrade yahoo_fin
sudo pip install html_requests

Use:
python api6_yahoo.py
"""
# import stock_info module from yahoo_fin
from yahoo_fin import stock_info as si
import datetime

def main():
	ticker = 'MSFT'								# microsoft
	today = datetime.date.today()

	print("Todays Date: " + str(today))

	# Get live price of Apple
	live = si.get_live_price("aapl")			# Apple ticker
	print("Live Price: %.2f" % live)			# <---- Could just use the live price!!


	# In a date range [month/day/year]
	#data = si.get_data(ticker , start_date = '04/01/2019' , end_date = '04/02/2019')
	#data = si.get_data(ticker , start_date = '05/10/2019' , end_date = today)
	#print(str(data))

	#new = data.open
	#print("Open: %.2f" % new)


if __name__ == "__main__": main()