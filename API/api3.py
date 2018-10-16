# -*- coding: utf-8 -*-
"""
Description:
URL request data retrieval returns byte type then converts to dictionary
and extracts opening bitcoin value

Note: Run in 'crypto' virtual environment  

Use:
python3 api3.py
"""
import datetime
import requests
import ast


def main():
	start = datetime.datetime(2017,1,1)
	end = datetime.date.today()

	# Make URL data request for daily bitcoin data 
	data = requests.get('https://www.bitstamp.net/api/v2/ticker/btcusd/')

	# Get byte format json content
	opening = data.content					# Get the full data line retrieved

	# convert to dictionary
	data = ast.literal_eval(opening.decode("utf-8"))

	# Use 'open' key to find opening price value
	print(data['open'])


if __name__ == "__main__": main()