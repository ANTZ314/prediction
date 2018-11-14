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
			# get csv file
			dataset = pd.read_csv('BTC[10_2018]_train.csv')

			# Get all values in column 2 (Open Price)
			opening = dataset.iloc[:,1:2].values     					
			
			# get the number of values
			size = len(opening)
			#size = 3
			print(str(size))
		except:
				print("ERROR...1")

		try:
			with open(r'test.csv', 'a', newline='') as csvfile:
			    fieldnames = ['Date','Open']
			    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

			    writer.writerow({'Date':today, 'Open':'Open Price'})
			    csvfile.close()
			    print(today)
		except:
			print("ERROR...2")

	except:
		print("MAIN EXCEPTION REACHED")


if __name__ == "__main__": main()