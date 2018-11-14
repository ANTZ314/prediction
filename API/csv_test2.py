# -*- coding: utf-8 -*-
"""
Description:
* Gets number of rows in column 2 = size
* Prints specified cell according to [col, row] (Note: Cells start at [0, 0])
* Gets yesterdays Opening & Direction
* Indicates Y/N for direction correct
* Shows Error Rate from yesterday to todays Opening price

Note: Run in 'crypto' virtual environment for 'pandas'

Use:
python csv_test.py
"""
import pandas as pd
import datetime
import csv

size = 0

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
    dataset = pd.read_csv('test.csv')
    # Get all values in column 2 (Open Price)
    opening = dataset.iloc[:,1:2].values
    # get the number of values
    size = len(opening)

    # print last open price
    #print("last: " + str(opening[(size-1)]))

    # Return the number of values
    return size

def main():
    Y_open = 0              # yesterdays predicted opening price
    Y_direct = "UP"         # yesterdays predicted direction
    Y_value = 0             # yesterdays float value
    YN_direct = "X"         # Yes/No Correct prediction indicator
    P_Error = 0             # Percent Error

    # test purposes
    T_open = 6224           # todays actual opening price
    T_direct = "DOWN"       # todays actual direction


    try:
        # Get the number of rows in the csv
        size = get_size()
        print("Number of Rows: " + str(size))

        # Read yesterdays Opening Price
        Y_open = read_cell(1, (size))
        print ("Yesterdays Opening: " + Y_open)

        # Read yesterdays Direction
        Y_direct = read_cell(6, (size-1))
        print ("Yesterdays Direction: " + Y_direct)

        # Predicted direction Correct?
        if Y_direct == T_direct:
            YN_direct = "Y"
            print("Correct: " + YN_direct)
        else:
            YN_direct = "N"
            print("Correct: " + YN_direct)


        # convert to float
        Y_value = float(Y_open)
        P_Error = ((Y_value - T_open) / T_open) * 100
        print("Error %: " + str(P_Error)) 
                    
    except:
        print("MAIN EXCEPTION REACHED")


if __name__ == "__main__": main()