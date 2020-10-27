# -*- coding: utf-8 -*-
"""
Description:
Using Quandl to retrieve bitcoin (BITSTAMP) data and then plot the 'Low' values from that data
Also prints first 3 lines of the data, and last 3 lines of data.
NOT THIS: Date | Open | High | Low | Close | Volume (BTC) | Volume (Currency) | Weighted Price
THIS----> High | Low | Last | Bid | Ask | Volume | VWAP

Note: 	Run in 'crypto' virtual environment  
		'q' to quit

Use:
python api2.py
"""
import datetime
import matplotlib.pyplot as plt
import quandl

def main():
	start = datetime.datetime(2017,1,1)
	end = datetime.date.today()

	#quandl.ApiConfig.api_key = "EfVSTGzAz3sxDyyG2Tqm"
	data = quandl.get("BITSTAMP/USD", start_date=start, end_date=end, api_key="EfVSTGzAz3sxDyyG2Tqm")
	print(data.head(3))				# first 3 data entries
	print(data.tail(3))				# last 3 lines (check date and colum headings)
	#data.Low.plot()				# 1st way: plot 'LOW' values
	#plt.plot(data['Low'])			# 2nd way: plot 'LOW' values
	plt.plot(data['High'])			# 
	
	# VISUALLISE #
	plt.title('- Quandl Data Plotter -')
	plt.xlabel('Time')
	plt.ylabel('Low Value')
	plt.legend()
	plt.show()
	

if __name__ == "__main__": main()