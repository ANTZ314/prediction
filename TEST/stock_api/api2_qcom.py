# -*- coding: utf-8 -*-
"""
Description:
* Using Quandl & Stock's "Ticker Symbol" to retrieve 
  the stock data and then plot the 'High' values on graph
* Also prints first & last 3 lines of the data.
* 'q' to quit

Note: 	Run in 'crypto' virtual environment
		Check Quandl API_KEY is still valid

Use:
python api2.py
"""
import datetime
import matplotlib.pyplot as plt
import quandl

def main():
	start = datetime.datetime(2017,1,1)
	end = datetime.date.today()

	## Stock ticker codes
	#s = "MSFT" 		# Microsoft
	#s = "QCOM" 		# Qualcomm
	s = "TSLA"			# Tesla
	#s = "AAPL"			# Apple

	#quandl.ApiConfig.api_key = "EfVSTGzAz3sxDyyG2Tqm"
	data = quandl.get("WIKI/" + s, start_date=start, end_date=end, api_key="EfVSTGzAz3sxDyyG2Tqm")
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