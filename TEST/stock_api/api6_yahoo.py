# -*- coding: utf-8 -*-
"""
Note: 
* Run in 'crypto' virtual environment  
* Link1: http://theautomatic.net/yahoo_fin-documentation/
* Link2: http://theautomatic.net/2018/07/31/how-to-get-live-stock-prices-with-python/

Dependencies:
sudo pip install yahoo_fin
sudo pip install --upgrade yahoo_fin
sudo pip install html_requests

Description:


Use:
python api6_yahoo.py
"""
# import stock_info module from yahoo_fin
from yahoo_fin import stock_info as si
import datetime

def main():
	ticker = 'MSFT'
	today = datetime.date.today()

	print("Todays Date: " + str(today))

	# Get live price of Apple
	live = si.get_live_price("aapl")
	print("Live Price: %.2f" % live)			# <---- Could just use the live price!!


	# In a date range [month/day/year]
	#data = si.get_data(ticker , start_date = '04/01/2019' , end_date = '04/02/2019')
	data = si.get_data(ticker , start_date = '05/11/2019' , end_date = today)
	print(str(data))

	new = data.open
	print("Open: %.2f" % new)

if __name__ == "__main__": main()