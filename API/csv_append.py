# -*- coding: utf-8 -*-
"""
Description:


Note: Run in 'crypto' virtual environment  

Use:
python3 api3.py
"""
import datetime
import csv


def main():
	try:
		start = datetime.datetime(2017,1,1)
		today = datetime.date.today()

		try:
			with open(r'test.csv', 'a', newline='') as csvfile:
			    fieldnames = ['Date','Open']
			    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

			    writer.writerow({'Date':today, 'Open':'Open Price'})
			    csvfile.close()
			    print(today)
		except:
			print("ERROR...")


	except:
		print("EXCEPTION REACHED")


if __name__ == "__main__": main()