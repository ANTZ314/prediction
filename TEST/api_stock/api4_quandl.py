# -*- coding: utf-8 -*-
"""
Description:
Quandl request data retrieval and extracts opening column between selected dates

NOTE!!
-- WIKI no longer updated from 2018-03-28 --

Columns:
Date | 

Note: Run in 'crypto' virtual environment  

Use:
python3 api3.py
"""
import datetime
import requests
import ast
import quandl


def main():
	start = datetime.datetime(2018,1,1)
	end   = datetime.date.today()

	# Request the first 5 rows
	data = quandl.get("WIKI/AAPL", rows=5)
	print(data)

	# Request specific columns of multiple stocks
	#data = quandl.get(["NSE/OIL.1", "WIKI/AAPL.4"])
	#print(data)
	
	# Request column 4 [Close] between now and 'start' date
	data = quandl.get("WIKI/TSLA.4", start_date=start, end_date=end)
	print(data)

	# Use 'open' key to find opening price value
	#print(data)
	#print("\nDate today: " + str(end))


if __name__ == "__main__": main()