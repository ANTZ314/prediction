# -*- coding: utf-8 -*-
"""
Description:
* URL request data retrieval from alpha-vantage
* Key: PBRGXKAUD9LKYI3Z
* output_format = 'pandas'/'csv'/'json' (JSON default)

Note: 
Run in 'crypto' virtual environment


Use:
python3 api3.py
"""
from alpha_vantage.timeseries import TimeSeries
from pprint import pprint

def main():
	ts = TimeSeries(key='PBRGXKAUD9LKYI3Z', output_format='pandas')
	data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
	pprint(data.head(2))

if __name__ == "__main__": main()