# -*- coding: utf-8 -*-
"""
Dependency:
* yahoo_finance_api2 (pip install)

Description:	----> DISCONTINUED???
* 

Note: 	Run in 'crypto' virtual environment

Use: 	python api1_yahoo.py
"""
import sys
from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError

def main():
	try:
		symbol_data = my_share.get_historical(share.PERIOD_TYPE_DAY, 10, share.FREQUENCY_TYPE_MINUTE, 5)	

	except YahooFinanceError as e:
		print(e.message)
		sys.exit(1)

	print(symbol_data)


if __name__ == "__main__": main()