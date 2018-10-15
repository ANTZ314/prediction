# -*- coding: utf-8 -*-
"""
Description:
Use 'fix_yahoo_finance' to retrieve Yahoo stock price and graph (general) data 

Use:
python api1.py
"""
import datetime
import matplotlib.pyplot as plt   	# Import matplotlib
import fix_yahoo_finance as yf


def main():
	start = datetime.datetime(2016,1,1)
	end = datetime.date.today()

	data = yf.download("AAPL", start, end)
	data.Close.plot()
	plt.title('Yahoo Closing Stock Price')
	plt.xlabel('Time')
	plt.ylabel('Value')
	plt.legend()
	plt.show()

if __name__ == "__main__": main()