# -*- coding: utf-8 -*-
"""
Description:
URL request data retrieval returns byte type then converts to dictionary
and extracts opening bitcoin value.
Checks for 'open.txt' file. If doesn't exist, creates it and writes to it.
If it exists, appends new Opening value with date.
Appends date and BTC_USD Opening value to csv file for re-training tomorrow.

Note: Run in 'crypto' virtual environment  

Use:
python3 api3.py
"""
import datetime
import requests
import ast
import csv


def main():
	exc = 'none'									# quick error code
	fl_open = 0.1									# Float value to work with

	try:
		#start = datetime.datetime(2017,1,1)
		today = datetime.date.today()

		# Make URL data request for daily bitcoin data 
		data = requests.get('https://www.bitstamp.net/api/v2/ticker/btcusd/')

		# Get byte format json content
		opening = data.content					# Get the full data line retrieved

		# convert to dictionary
		data = ast.literal_eval(opening.decode("utf-8"))

		# Use 'open' key to find opening price value
		print("Date: " + str(today))
		print("Opening price: " + data['open'])
		#print(type(data['open']))

		#convert to float
		fl_open = float(data['open'])
		#print(type(fl_open))

		try:
			exc = 'Error: text file'
			# If the file exists
			file = open('open.txt', 'a+') 					# Open to read file
			file.write("\nDate: " + str(today) + " - Opening: " + data['open']
			 + " - High: " + data['high'] + " - Low: " + data['low'] + " - Close: " + data['last'])
			print("File found and writen to...")
			file.close()									# Close the file

			exc = 'Error: writing to CSV'
			with open(r'test.csv', 'a', newline='') as csvfile:
			    fieldnames = ['Date','Open','High','Low','Close']
			    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			    writer.writerow({'Date':today, 'Open':data['open'], 'High':data['high'], 'Low':data['low'], 'Close':data['last']})
			    csvfile.close()

		except:
			print(exc)

	except:
		print("EXCEPTION REACHED WHILE RETRIVING DATA")


if __name__ == "__main__": main()