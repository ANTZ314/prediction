
"""
#~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Recurrent Neural Network #
#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~#
# Code Functionality #
#~~~~~~~~~~~~~~~~~~~~#
* Gets trainging data 'csv' file and checks the size of column 2 (Opening Price)		[x]
* Using the size of the column it trains the LSTM up to the last value stored			[x]
* Make URL request (Bitstamp) for todays Bitcoin data (byte format)						[x]
* Extracts the latest 'Open' value as the "real_stock_price" for the prediction method	[x]
* Print predicted value to text file for comparison to tomorrows price (accuracy)		[-] 
* Append Todays Data to last Row of CSV for tomorrows evaluation 						[-]

Note:
VirtualEnv: workon crypto

Dataset used BTCUSD from https://www.cryptodatadownload.com/ (Bitstamp)
"""


# Importing the libraries
import numpy as np                								# To make the arrays. Only input allowed to NN (as apposed to data-frames)
import matplotlib.pyplot as plt    								# Used to visualise the results at the end
import pandas as pd               						 		# To import the dataset and manage them easily
## Importing the Keras libraries and packages ##
from keras.models import Sequential     						# Initialise the RNN
from keras.layers import Dense          						# Creates the output layer of RNN
from keras.layers import LSTM           						# Type of RNN - Long Term Memory (Best)
## Import general purpose libraries
import datetime
import requests
import ast
import csv

## GLOBALS ##
size = 0

####################
## READ CSV CELLS ##
####################
def read_cell(x, y):
    with open('BTCUSD.csv', 'r') as file:
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
    print("here")
    with open('BTCUSD.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['John Smith', 'Accounting', 'November'])

#########################
## GET SIZE OF THE CSV ##
#########################
def get_size():
    # get csv file
    dataset = pd.read_csv('BTCUSD.csv')
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
	#################################
	## Part 1 - Data Preprocessing ##
	#################################
	## Importing the training set ##
	dataset_train = pd.read_csv('BTCUSD.csv') 					# Get the .csv file
	training_set = dataset_train.iloc[:,1:2].values     		# Get all values in column 2 (Open Price)
	# get the number of values
	train_size = len(training_set)								# print(str(size))

	## Apply Feature Scaling ##
	from sklearn.preprocessing import MinMaxScaler  			# import the class
	sc = MinMaxScaler()                             			# create an object of the class with default input
	training_set = sc.fit_transform(training_set)   			# modify training set by fitting and transforming
	## Getting the inputs and the ouputs ##
	X_train = training_set[0:(train_size-1)]  					# get all stock prices except last one (time -> t)
	y_train = training_set[1:train_size]  						# all stock prices shifted by one (time -> t+1)
	## Reshaping ##
	X_train = np.reshape(X_train, ((train_size-1), 1, 1))

	###############################
	## Part 2 - Building the RNN ##
	###############################
	fl_open = 0.1															# Opening Price (float) extracted from todays API 

	## Initialising the RNN ##
	regressor = Sequential()                								# Create object for RNN model in a sequence of layers
	## Adding the input layer and the LSTM layer ##
	regressor.add(LSTM(units = 4, activation = 'sigmoid', input_shape = (None, 1)))
	## Adding the output layer ##
	regressor.add(Dense(units = 1))     									# All default values & 1 input
	## Compiling the RNN ##
	regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')
	## Fitting the RNN to the Training set ##
	regressor.fit(X_train, y_train, batch_size = 32, epochs = 200)
	
	###########################################################
	## Part 3 - Get todays 'Open' value & convert to Integer ##
	###########################################################
	print("Fetching todays BTCUSD data from Bitstamp...")

	try:
		today = datetime.date.today()										# get todays date

		# Make URL data request for daily bitcoin data 
		data = requests.get('https://www.bitstamp.net/api/v2/ticker/btcusd/')	# Make URL data request

		# Get byte format json content
		opening = data.content												# Get the full data line retrieved ('byte' format)

		# convert 'byte' to dictionary (strings)
		data = ast.literal_eval(opening.decode("utf-8"))

		#convert to float
		fl_open = float(data['open'])										# Check: print(type(fl_open))
	except:
		print("API/URL retrieval Error...")

	real_stock_price = fl_open												# todays Opening Price (float)

	#############################################################
	## Part 4 - Making the predictions using todays Open Price ##
	#############################################################
	inputs = real_stock_price                                               # Use the 
	inputs = sc.transform(inputs)                                           # Scale the inputs to match scale used for training
	inputs = np.reshape(inputs, (1, 1, 1))                                  # Change to 3 dimensional array
	predicted_stock_price = regressor.predict(inputs)                       # give you the predicted price for that month
	predicted_stock_price = sc.inverse_transform(predicted_stock_price)     # scale back to original price values

	#print("\nDate: \t\t\t[[" + str(today) + "]]")
	#print("Opening Price: \t\t[[" + str(real_stock_price) + "]]")			# Print value
	#predicted_stock_price = format(predicted_stock_price, '.2f')			# Round to 2 decimal
	#print("Predicted Price: \t" + str(predicted_stock_price))				# Print value
	
	###################################################
	## Part 5 - Analyse Predictions vs Actual Values ##
	###################################################
	YP_open  = 0             		# Yesterdays Predicted opening price    - [5,size]
	Y_direct = "none"				# Yesterdays Predicted Direction		- [7,size]
	T_Pred   = "none"				# Tomorrows Predicted Price
	Y_value  = 0.1             		# Yesterdays Predicted Value (float)
	T_direct = "none"				# actual direction (UP/DOWN)
	diff     = 0.1					# difference btwn predicted & actual value
	Tom_dir  = "none"				# Tomorrows Predicted Direction
	YN_direct = "X"					# Correct prediction indicator
	P_Error  = 1.11          		# Percent Error                         - Calculated

	try:
		# Get the number of rows in the csv
		size = get_size()
		#print("Number of Rows: " + str(size))

		# Read yesterdays Predicted Opening Price (Column F: ERROR IF NO VALUE)
		YP_open = read_cell(5, (size))
		#print("Yesterdays Opening:\t" + YP_open)

		# Read yesterdays Direction
		Y_direct = read_cell(7, (size))
		#print("Yesterdays Predicted Direction:\t" + Y_direct)
		

		if YP_open == "none":
			print("No predicted price found for yesterday...")
		else:
			## Yesterday to Todays Direction
			Y_value = float(YP_open)						# convert to float
			diff = Y_value - real_stock_price
			if diff > 0:
				T_direct = "DOWN"
			else:
				T_direct = "UP"
		
		## Today to Tomorrows Direction
		diff = real_stock_price - predicted_stock_price
		if diff > 0:
			Tom_dir = "DOWN"
		else:
			Tom_dir = "UP"

		if YP_open == "none":
			print("No direction found for yesterday...")
		else:
			# Predicted direction Correct?
			if Y_direct == T_direct:
				YN_direct = "Y"
				#print("Correct: " + YN_direct)
			else:
				YN_direct = "N"

		if YP_open == "none":
			print("Error can't be calculated without yesterdays predicted value...")
		else:
			# Convert to float for Error Rate
			Y_value = float(YP_open)
			P_Error = ((Y_value - real_stock_price) / real_stock_price) * 100
			P_Error = format(P_Error, '.4f')
			#print("Error %: " + str(P_Error))

		T_Pred = str(predicted_stock_price)
		T_Pred = T_Pred.strip("[]")

		# PRINT OUT ALL VALUES TO THE CONSOLE
		print ("\nDate: \t\t\t\t" + str(today))
		print ("\nYesterdays Predicted Open:\t" + str(YP_open))
		print ("Todays Actual Open:\t\t" + str(real_stock_price))
		print ("Error Rate:\t\t\t" + str(P_Error) + " %")
		print ("Tomorrows Predicted Opening:\t" + T_Pred)
		print ("=================================\n")
		print ("Yesterdays Predicted Direction:\t" + Y_direct)
		print ("Todays Actual Direction:\t" + T_direct)
		print ("Correct:\t\t\t" + YN_direct)
		print ("=================================\n")
		print ("Tomorrows Predicted Direction:\t" + Tom_dir)

	except:
		print ("Analytics Error!")

	######################################################################
	## Part 6 - Write the new results to text and csv file for tomorrow ##
	######################################################################
	
	exc = "none"															# exception message
	try:
		# Write to TEXT #
		exc = 'text file'													# Ecxeption error message
		# If the file exists
		file = open('open.txt', 'a+') 										# Open to write to file
		file.write("\nDate: " + str(today) + " - Opening: [[" + str(real_stock_price) + "]]"
		+ " - Predicted: " + str(predicted_stock_price))
		file.close()														# Close the file

		# Write to CSV #
		exc = 'writing to CSV'												# Ecxeption error message
		with open(r'BTCUSD.csv', 'a', newline='') as csvfile:				# open to write to file
		    fieldnames = ['Date','Open','High','Low','Close','P_Open','Error','Pred_Dir','Act_Dir','Correct']
		    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		    writer.writerow({'Date':today, 'Open':data['open'], 'High':data['high'], 'Low':data['low'], 
		    	'Close':data['last'],'P_Open':str(T_Pred), 'Error':str(P_Error), 
		    	'Pred_Dir':Tom_dir, 'Act_Dir':T_direct, 'Correct':YN_direct})
		    csvfile.close()
		exc = "none"
		print("\nComplete...\n")

	except:
		print("Error: " + exc)
	
	####################################################################
	## Part 6 - Compare yesterday's Predicted Price with Todays Price ##
	####################################################################
	# Accuracy


if __name__ == "__main__": main()