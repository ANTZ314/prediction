# -*- coding: utf-8 -*-
"""
Description:
URL request data retrieval returns byte type then converts to dictionary
and extracts opening bitcoin value.
Checks for 'open.txt' file. If doesn't exist, creates it and writes to it.
If it exists, appends new Opening value with date.

Note: Run in 'crypto' virtual environment  

Use:
python3 api3.py
"""
import datetime
import requests
import ast


def main():
	try:
		start = datetime.datetime(2017,1,1)
		end = datetime.date.today()

		# Make URL data request for daily bitcoin data 
		data = requests.get('https://www.bitstamp.net/api/v2/ticker/btcusd/')

		# Get byte format json content
		opening = data.content					# Get the full data line retrieved

		# convert to dictionary
		data = ast.literal_eval(opening.decode("utf-8"))

		# Use 'open' key to find opening price value
		print("Date: " + str(datetime.date.today()))
		print("Opening price: " + data['open'])
		try:
			# If the file exists
			file = open('open.txt', 'a+') 					# Open to read file
			file.write("\nDate: " + str(datetime.date.today()) + " - Opening price: " + data['open'])
			print("File writen to...")
			file.close()									# Close the file
		except:
			# If the file didn't exist
			file= open("open.txt","a+")						# Create & open the file, then Append data 
			file.write("BTC_USD Opening Price API: \n\n")
			file.write("\nDate: " + str(datetime.date.today()) + " - Opening price: " + data['open'])
			print("File created & written to...")
			file.close()									# Exit the opened file


	except:
		print("EXCEPTION REACHED WHILE RETRIVING DATA")


if __name__ == "__main__": main()