# -*- coding: utf-8 -*-
"""
Description:

Note:
VirtualEnv: workon crypto
"""
## Import general purpose libraries
import datetime												# Crypto current date
#import requests												# Used for Crypto
import ast
import csv

## GLOBALS ##
size = 0

####################
## READ CSV CELLS ##
####################
def read_cell(x, y):
    with open('QCOM.csv', 'r') as file:
        reader = csv.reader(file)
        y_count = 0
        for n in reader:
            if y_count == y:
                cell = n[x]
                return cell
            y_count += 1

#########################
## WRITE DATA TO CELLS ##
#########################
def write_cell():
    with open('QCOM.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['John Smith', 'Accounting', 'November'])

#########################
## GET SIZE OF THE CSV ##
#########################
def get_size():
    # get csv file
    dataset = pd.read_csv('QCOM.csv')
    # Get all values in column 2 (Open Price)
    opening = dataset.iloc[:,1:2].values
    # get the number of values
    size = len(opening)

    #print("last: " + str(opening[(size-1)]))					# Show last open price

    # Return the number of values
    return size

###################
## MAIN FUNCTION ##
###################
def main():
	
		today = '2019/05/20'
		YP_open = '22222'
		real_stock_price = 33.11
		predicted_stock_price = 44.22
		P_Error = '1.11'
		Tom_dir = 'DOWN'
		T_Pred = '77.5'
		Y_direct = '77777'
		T_direct = 'UP'
		YN_direct = 'NO'

		open1 = '57.46'
		close1 = '70.45'
		high1 = '71.03'
		low1 = '57.29'

	#try:
		# PRINT OUT ALL VALUES TO THE CONSOLE
		print ("\nDate: \t\t\t\t" + str(today))
		print ("\nYesterdays Predicted Open:\t" + str(YP_open))
		print ("Todays realtime price:\t\t%.2f" % real_stock_price)
		print ("Error Rate:\t\t\t" + str(P_Error) + " %")
		print ("Tomorrows Predicted Opening:\t" + T_Pred)
		print ("Tomorrows Predicted Direction:\t" + Tom_dir)
		print ("=================================\n")
		print ("Yesterdays Predicted Direction:\t" + Y_direct)
		print ("Todays Actual Direction:\t" + T_direct)
		print ("Correct:\t\t\t" + YN_direct)
		print ("=================================\n")

	#except:
	#	print ("Analytics Error!")

	######################################################################
	## Part 6 - Write the new results to text and csv file for tomorrow ##
	######################################################################
	
	#exc = "none"															# exception message
	#try:
		# Write to TEXT #
		exc = 'text file'													# Ecxeption error message
		# If the file exists
		file = open('open.txt', 'a+') 										# Open to write to file
		file.write("\nDate: " + str(today) + " - Opening: [[" + str(real_stock_price) + "]]"
		+ " - Predicted: " + str(predicted_stock_price))
		file.close()														# Close the file
		print("Text File Complete...")

		# Write to CSV #
		exc = 'writing to CSV'												# Ecxeption error message
		with open(r'QCOM.csv', 'a') as csvfile:					# open to write to file
		    fieldnames = ['Date','Open','High','Low','Close','P_Open','Error','Pred_Dir','Act_Dir','Correct']
		    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		    
		    writer.writerow({'Date':today, 'Open':open1, 'High':high1, 'Low':low1, 
		    	'Close':close1,'P_Open':str(T_Pred), 'Error':str(P_Error), 
		    	'Pred_Dir':Tom_dir, 'Act_Dir':T_direct, 'Correct':YN_direct})

		    csvfile.close()
		exc = "none"
		print("\nCSV File Complete...\n")

	#except:
	#	print("Error: " + exc)
	
	####################################################################
	## Part 6 - Compare yesterday's Predicted Price with Todays Price ##
	####################################################################
	# Accuracy


if __name__ == "__main__": main()