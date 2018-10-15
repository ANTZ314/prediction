#~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Recurrent Neural Network #
#~~~~~~~~~~~~~~~~~~~~~~~~~~#

## Using an LSTM to predict the upward/downward trend of the Google Stock Price ##
# -> Trained on 5 years of Google stock data (2012-2016)
# -> Then try to predict upward/downward trend of January 2017

# A Regression Model is a model that predicts a continuous outcome
# 
# * After using the training set, this model will use the current day's stock price 't'
# * to predict the following days stock price 't+1'. In practice you would therefore have
# * to wait for the price of each day to input before getting a prediction for tomorrow.
#
# -> Basically mimics short term memory
# -> Add a time dimension to the layers of a neural network

#################################
## Part 1 - Data Preprocessing ##
#################################

# Importing the libraries
import numpy as np                 # To make the arrays. Only input allowed to NN (as apposed to data-frames)
import matplotlib.pyplot as plt    # Used to visualise the results at the end
import pandas as pd                # To import the dataset and manage them easily

## Importing the training set ##
dataset_train = pd.read_csv('BTC[10_2018]_train.csv') 		# Get the .csv file
training_set = dataset_train.iloc[:,1:2].values     		# Get all lines in column 2 (Open Price)
## Apply Feature Scaling ##
from sklearn.preprocessing import MinMaxScaler  			# import the class
sc = MinMaxScaler()                             			# create an object of the class with default input
training_set = sc.fit_transform(training_set)   			# modify training set by fitting and transforming
## Getting the inputs and the ouputs ##
X_train = training_set[0:1140]  # get all stock prices except last one (time -> t)
y_train = training_set[1:1141]  # all stock prices shifted by one (time -> t+1)
## Reshaping ##
X_train = np.reshape(X_train, (1140, 1, 1))

###############################
## Part 2 - Building the RNN ##
###############################

## Importing the Keras libraries and packages ##
from keras.models import Sequential     # Initialise the RNN
from keras.layers import Dense          # Creates the output layer of RNN
from keras.layers import LSTM           # Type of RNN - Long Term Memory (Best)

## Initialising the RNN ##
regressor = Sequential()                # Create object for RNN model in a sequence of layers
## Adding the input layer and the LSTM layer ##
regressor.add(LSTM(units = 4, activation = 'sigmoid', input_shape = (None, 1)))
## Adding the output layer ##
regressor.add(Dense(units = 1))     # All default values & 1 input
## Compiling the RNN ##
regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')
## Fitting the RNN to the Training set ##
regressor.fit(X_train, y_train, batch_size = 32, epochs = 200)

#################################################################
## Part 3 - Making the predictions and visualising the results ##
#################################################################

# Getting the real stock price of 2017 ##
test_set = pd.read_csv('BTC[10_2018]_test.csv')                               # Get the real stock price dataset 
real_stock_price = test_set.iloc[:,1:2].values                          # Get all the rows in column 1

inputs = real_stock_price                                               # Use the 
inputs = sc.transform(inputs)                                           # Scale the inputs to match scale used for training
inputs = np.reshape(inputs, (31, 1, 1))                                 # Change to 3 dimensional array
predicted_stock_price = regressor.predict(inputs)                       # give you the predicted price for month of Jan
predicted_stock_price = sc.inverse_transform(predicted_stock_price)     # scale back to original price values

# Visualising the results ##
plt.plot(real_stock_price, color = 'red', label = 'Real BTC to USD Price')
plt.plot(predicted_stock_price, color = 'blue', label = 'Predicted BTC to USD Price')
plt.title('Google Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Google Stock Price')
plt.legend()
plt.show()

#################################
## Part 4 - Evaluating the RNN ##
#################################
# -> Regression models are evaluated by computing the RMSE (Root Mean Square Error) of the test set

import math # to get the root of the function
from sklearn.metrics import mean_squared_error # to get the mean squared error function

# To get the RMSE between the real and the predicted values
# To evaluate the performance of the model on new observations
rmse = math.sqrt(mean_squared_error(real_stock_price, predicted_stock_price))

# Need to get the result in a % of the original value
# -> generally a good RMSE is below 1%
# -> based on the values in 'real_stock_price' table the average is approximately 800
precent = rmse / 800

###############################################################################
###############################################################################
####                            HOMEWORK                                   ####
###############################################################################
###############################################################################
# -> After running Part 1 to Part 3

####################################################
## Get the real Google Stock Price of 2012 - 2016 ##
####################################################
## Importing the training set ##
real_stock_price_train = pd.read_csv('BTC[10_2018]_test.csv') 
real_stock_price_train = real_stock_price_train.iloc[:,1:2].values


#########################################################
## Get the predicted Google Stock Price of 2012 - 2016 ##
#########################################################
# -> Already have the inputs contained in 'x_train' which has also already been
#    processed, meaning it was scaled and then re-shaped above, so we can use directly
predicted_stock_price_train = regressor.predict(X_train)
# -> 'x_train' is scaled, so the predictions will be scaled
# -> therefore we must unscale to get original scale
predicted_stock_price_train = sc.inverse_transform(predicted_stock_price_train)

#############################
## Visualising the results ##
#############################
plt.plot(real_stock_price_train, color = 'red', label = 'Real BTC Price')
plt.plot(predicted_stock_price_train, color = 'blue', label = 'Predicted Google Stock Price')
plt.title('Google Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Google Stock Price')
plt.legend()
plt.show()
