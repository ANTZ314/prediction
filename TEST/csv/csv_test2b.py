# -*- coding: utf-8 -*-
"""
Description:
* Gets number of rows in column 2 = size
* Prints specified cell according to [col, row] 
  (Note: Cells start at [0, 0])
* Gets yesterdays Opening & Direction from csv
* Indicates Y/N for direction correct
* Shows Error Rate from yesterday to todays Opening price
* Write results to CSV file last row

Note: Run in 'crypto' virtual environment for 'pandas'

Use:
python csv_test.py
"""
import pandas as pd
import datetime
import csv

def main():
    today = datetime.date.today()

    print("\nWrite:")

    with open(r'test.csv', 'a') as csvfile:
        fieldnames = ['Date','Open','High','Low','Close','Vol1','Vol2']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow({'Date':today, 'Open':'00', 'High': '11','Low': '22','Close': '33','Vol1': '44','Vol2': '55'})
        csvfile.close()

    print("Done...")


if __name__ == "__main__": main()