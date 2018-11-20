# -*- coding: utf-8 -*-
"""
Description:
* Gets number of rows in column 2 = size
* Prints specified cell according to [col, row] (Note: Cells start at [0, 0])
* Gets yesterdays Opening & Direction
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

size = 0

def read_cell(x, y):
    with open('test.csv', 'r') as file:
        reader = csv.reader(file)
        y_count = 0
        for n in reader:
            if y_count == y:
                cell = n[x]
                return cell
            y_count += 1

def write_cell():
    print("here")
    with open('test.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['John Smith', 'Accounting', 'November'])


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
    YP_open = 0             # Yesterdays Predicted opening price    - [5,size]
    YA_open = 0             # yesterdays Actual opening price       - [1,size]
    Y_value = 0             # Yesterdays float value                

    YP_direct = "UP"        # Yesterdays Predicted Direction        - [7,size]
    YA_direct = "UP"        # Yesterdays Actual direction           - [8,size]
    YN_direct = "X"         # Yes/No Correct prediction indicator   - Determined
    P_Error = 1.05          # Percent Error                         - Calculated

    # test purposes
    T_value = 6224.35       # Todays Actual opening price (test)    - Retrieved today
    T_direct = "down"       # Todays actual direction     (test)    - Determined from todays price
    diff = 1.05

    try:
        # Get the number of rows in the csv
        size = get_size()
        print("Number of Rows: " + str(size))

        # Read yesterdays Opening Price
        YP_open = read_cell(1, (size))
        print ("Yesterdays Opening: " + YP_open)

        # Read yesterdays Direction
        Y_direct = read_cell(7, (size))
        print ("Yesterdays Direction: " + Y_direct)

        # Find todays direction
        Y_value = float(YP_open)
        #T_value = float(T_open)
        diff = Y_value - T_value
        if diff > 0:
            T_direct = "down"
        else:
            T_direct = "up"

        print("Todays Opening: " + str(T_value))
        print("Todays Direct: " + T_direct)
        
        # Predicted direction Correct?
        if Y_direct == T_direct:
            YN_direct = "Y"
            print("Correct: " + YN_direct)
        else:
            YN_direct = "N"
            print("Correct: " + YN_direct)

        # convert to float for Error Rate
        Y_value = float(YP_open)
        P_Error = ((Y_value - T_value) / T_value) * 100
        P_Error = format(P_Error, '.4f')
        print("Error %: " + str(P_Error))

        # Write results back to CSV
        #write_cell()
        print("done")
                    
    except:
        print("MAIN EXCEPTION REACHED")


if __name__ == "__main__": main()