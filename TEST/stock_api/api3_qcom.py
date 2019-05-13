# -*- coding: utf-8 -*-
"""
Description:
* URL request data retrieval from Yahoo Finance 
* Returns and prints date / Close price since beginning of the year. 

Note: Run in 'crypto' virtual environment  

Use:
python3 api3.py
"""
import datetime
import requests
import ast

company = 'name'

def get_symbol(symbol):
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(symbol)

    result = requests.get(url).json()

    for x in result['ResultSet']['Result']:
        if x['symbol'] == symbol:
            #return x['name']
            company = x['name']
            date = x['open']

def main():
	#start = datetime.datetime(2017,1,1)
	#end = datetime.date.today()

	# Make URL data request for daily bitcoin data 
	#data = requests.get('http://chartapi.finance.yahoo.com/instrument/1.0/BHP.ax/chartdata;type=quote;range=1d/csv')
	
	# Get byte format json content
	#opening = data.content					# Get the full data line retrieved

	# convert to dictionary
	#data = ast.literal_eval(opening.decode("utf-8"))

	# Use 'open' key to find opening price value
	#print("Opening price: " + data['open'])
	company = get_symbol("MSFT")				# Microsoft
	print(company)

if __name__ == "__main__": main()