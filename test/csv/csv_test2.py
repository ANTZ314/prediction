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
    with open('test.csv', 'w') as file:
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

    YP_direct = "None"      # Yesterdays Predicted Direction        - [7,size]
    YA_direct = "None"      # Yesterdays Actual direction           - [8,size]
    YN_direct = "X"         # Yes/No Correct prediction indicator   - Determined
    P_Error = 1.05          # Percent Error                         - Calculated

    # test purposes
    T_value = 6124.35       # Todays Actual opening price (test)    - Retrieved today
    T_StrVal = "val"        # string to store
    T_Pred = 6665.31        # Prediction for tomorrow
    T_StrPred = "val"       # string to store
    T_direct = "None"       # Todays actual direction     (test)    - Determined from todays price
    Tom_dir = "None"        # Tomrrows Predicted Direction
    diff = 1.05             # Difference between predicted & real price

    try:
        # Todays Date
        today = datetime.date.today()

        # Get the number of rows in the csv
        size = get_size()
        print("Number of Rows: " + str(size))

        # Read yesterdays Predicted Opening Price
        YP_open = read_cell(1, (size))

        # Read yesterdays Direction
        Y_direct = read_cell(7, (size))

        # Yesterday to Todays Direction
        Y_value = float(YP_open)
        #T_value = float(T_open)
        diff = Y_value - T_value
        if diff > 0:
            T_direct = "DOWN"
        else:
            T_direct = "UP"

        # Today to Tomorrows Direction
        diff = T_value - T_Pred
        if diff > 0:
            Tom_dir = "DOWN"
        else:
            Tom_dir = "UP"

        print ("Yesterdays Opening:\t" + YP_open)
        print ("Todays Opening:\t\t" + str(T_value))
        print ("Yesterdays Predicted Direction:\t" + Y_direct)
        print ("Todays Actual Direction:\t" + T_direct)
        print ("Tomorrows Predicted Direction:\t" + Tom_dir)
        
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

        # Convert all values to string for storage
        T_StrVal = str(T_value)   # Todays actual opening price
        T_StrPred = str(T_Pred)   # Predicted Opening price for tomorrow
        #Error = str(P_Error)

        # Write results back to CSV
        exc = 'writing to CSV'                                              # Ecxeption error message
        with open(r'test.csv', 'a') as csvfile:                 # open to write to file
            fieldnames = ['Date','Open','High','Low','Close', 'P_Open', 'Error', 'Pred_Dir', 'Act_Dir', 'Correct']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writerow({'Date':today, 'Open':T_StrVal, 'High':T_StrVal, 'Low':T_StrVal, 
                'Close':T_StrVal, 'P_Open':T_StrPred, 'Error':str(P_Error), 'Pred_Dir':Tom_dir, 
                'Act_Dir':T_direct, 'Correct':YN_direct})

            csvfile.close()
        exc = "none"
        print("\nComplete...\n")
                    
    except:
        print("MAIN EXCEPTION REACHED")


if __name__ == "__main__": main()