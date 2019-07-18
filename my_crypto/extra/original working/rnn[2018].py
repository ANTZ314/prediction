
"""
#~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Recurrent Neural Network #
#~~~~~~~~~~~~~~~~~~~~~~~~~~#

## Using an LSTM to predict the upward/downward trend of the Google Stock Price ##
-> Trained on 5 years of Google stock data (2012-2016)
-> Then try to predict upward/downward trend of January 2017

A Regression Model is a model that predicts a continuous outcome
 
* After using the training set, this model will use the current day's stock price 't'
* to predict the following days stock price 't+1'. In practice you would therefore have
* to wait for the price of each day to input before getting a prediction for tomorrow.

#~~~~~~~~~~~~~~~~~~~~#
# Code Functionality #
#~~~~~~~~~~~~~~~~~~~~#
* Gets trainging data 'csv' file and checks the size of column 2 (Opening Price)
* Using the size of the column it trains the LSTM up to the last value stored
* Make URL request for yesterdays Bitcoin data and extracts the latest 'Open' value
* Uses this value as the "real_stock_price" for the prediction method
* Print predicted value to text file and append to column 2 for tomorrows evaluation 
"""

#################################
## Part 1 - Data Preprocessing ##
#################################

# Importing the libraries
import numpy as np                 # To make the arrays. Only input allowed to NN (as apposed to data-frames)
import matplotlib.pyplot as plt    # Used to visualise the results at the end
import pandas as pd                # To import the dataset and manage them easily

## Importing the training set ##
dataset_train = pd.read_csv('BTC[10_2018]_train.csv') 	# Get the .csv file
training_set = dataset_train.iloc[:,1:2].values     	# Get all values in column 2 (Open Price)
## Apply Feature Scaling ##
from sklearn.preprocessing import MinMaxScaler  		# import the class
sc = MinMaxScaler()                             		# create an object of the class with default input
training_set = sc.fit_transform(training_set)   		# modify training set by fitting and transforming
## Getting the inputs and the ouputs ##
X_train = training_set[0:1822]  # get all stock prices except last one (time -> t)
y_train = training_set[1:1823]  # all stock prices shifted by one (time -> t+1)
## Reshaping ##
X_train = np.reshape(X_train, (1822, 1, 1))

###############################
## Part 2 - Building the RNN ##
###############################

## Importing the Keras libraries and packages ##
from keras.models import Sequential     								# Initialise the RNN
from keras.layers import Dense          								# Creates the output layer of RNN
from keras.layers import LSTM           								# Type of RNN - Long Term Memory (Best)

exists = 0																# append after printing contents

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

#################################################################
## Part 3 - Making the predictions and visualising the results ##
#################################################################

# Getting the real stock price of 2017 ##
#test_set = pd.read_csv('BTC[10_2018]_test.csv')                         # Get the real stock price dataset 
#real_stock_price = test_set.iloc[:,1:2].values                          # Get all the values in column 2

real_stock_price = 6572.6		# todays price

inputs = real_stock_price                                               # Use the 
inputs = sc.transform(inputs)                                           # Scale the inputs to match scale used for training
inputs = np.reshape(inputs, (1, 1, 1))                                 # Change to 3 dimensional array
predicted_stock_price = regressor.predict(inputs)                       # give you the predicted price for that month
predicted_stock_price = sc.inverse_transform(predicted_stock_price)     # scale back to original price values

print (predicted_stock_price)

"""
# Write to file #
try:																	# Skip if file doesn't exist
	file = open('predicted.txt', 'r') 									# Open to read file
	print (file.read())													# Print the contents
	file.close()														# Close the file
except:
	exists = 1															# Don't append twice if file exists
	file= open("predicted.txt","a+")									# Create/open file then Append data 
	file.write(str(predicted_stock_price))								# Write the predicted values to the trext file
	file.close()														# Exit the opened file

if exists == 0:															# append after printing contents
	file= open("predicted.txt","a+")									# Create/open file then Append data
	file.write(str(predicted_stock_price))								# Write the predicted values to the trext file
	file.close()														# Exit the opened file
else:																	# 
	print ("\nFile Didn't exist... Now it does!")						# notification	

"""