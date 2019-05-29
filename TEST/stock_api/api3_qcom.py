# -*- coding: utf-8 -*-
"""
Description:
* URL request data retrieval from Yahoo Finance 
* Company name of ticker provided

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
            return x['name']
            #company = x['name']
            #date = x['open']

def main():
	company = get_symbol("MSFT")				# Microsoft
	print(company)

if __name__ == "__main__": main()