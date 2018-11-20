# -*- coding: utf-8 -*-
"""
Description:
* Retrieve all missing previous dates
	-> Get last date and compare todays date
	-> Retrieve each missing days data string
	-> Add each day (in format) into CSV
	-> Do comparisons and add to csv also

Note: Run in 'crypto' virtual environment for 'pandas'
Use: python csv_test3.py

"""
import pandas as pd
import datetime
import csv

file_name = 'test.csv'

def read_cell(x, y):
    with open('test.csv', 'r') as f:
        reader = csv.reader(f)
        y_count = 0
        for n in reader:
            if y_count == y:
                cell = n[x]
                return cell
            y_count += 1

def get_size():
    # get csv file
    dataset = pd.read_csv(file_name)
    # Get all values in column 2 (Open Price)
    opening = dataset.iloc[:,1:2].values
    # get the number of values
    size = len(opening)
    # Return the number of values
    return size

def main():
	missing = 0

	try:
		# Get the number of rows
		size = get_size()									# Get the number of rows in the csv

		# Get todays date
		todays_Date = datetime.date.today()					# Get the date
		print ("Todays date: " + str(todays_Date))

		# get last stored date
		last_Date = read_cell(0, (size))					# Get last date cell
		last_Date = datetime.date(*(int(s) for s in last_Date.split('-')))	# Convert to datetime format
		print ("Last stored date: " + str(last_Date))

		# compare to see how many days missing
		if (todays_Date > last_Date):
			missing = todays_Date - last_Date
			#print(str(missing))
			missing = missing.days
			print("Missing days: " + str(missing))
		else:
			print("Up to date...")

		# Retrieve each missing day up to & store to csv
		while(missing >= 0):
			print(str(missing))
			missing -= 1


	except:
		print("MAIN EXCEPTION REACHED")


if __name__ == "__main__": main()