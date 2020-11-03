# -*- coding: utf-8 -*-
"""
Description:
Open csv file & Reads values from column 2
Print the number of values (number of rows in col2)
Append date and 'string' to last row of first 2 columns

Note: Run in 'crypto' virtual environment  

Use:
python3 csv_test.py
"""
import pandas as pd
import datetime
import csv


def main():
	try:
		today = datetime.date.today()

		try:
			print("Read:")
			# get csv file
			#dataset = pd.read_csv('BTC[10_2018]_train.csv')
			dataset = pd.read_csv('test.csv')

			# Get all values in column 2 (Open Price)
			opening = dataset.iloc[:,1:2].values     					
			
			# get the number of values
			size = len(opening)
			#size = 3
			print("Rows: " + str(size))
		except:
				print("ERROR...1")

		try:
			print("\nWrite:")

			with open(r'test.csv', 'a') as csvfile:
			    fieldnames = ['Date','Open','High','Low','Close','Vol1','Vol2']
			    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

			    writer.writerow({'Date':today, 'Open':'00', 'High': '11','Low': '22','Close': '33','Vol1': '44','Vol2': '55'})
			    csvfile.close()
			    print(today)

			print("Done...")
		except:
			print("ERROR...2")

	except:
		print("MAIN EXCEPTION REACHED")


if __name__ == "__main__": main()