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
# -> this makes a data_frame which must then be converted to an array
training_set = pd.read_csv('Google_Stock_Price_Train.csv') # Get the .csv file
# -> Not only select the right column (Open Google Stock price)
# -> But also make it a numpy array (input to NN must be np.array in keras)
# -> Requires an array so [1:2] makes a 2 dimensional array with only 1 index (python excludes upper index)
# -> 'iloc' method gets the selected index we want
training_set = training_set.iloc[:,1:2].values             # Get all lines in column 1

## Apply Feature Scaling ##
# -> Could use either 'Standardisation' or 'Normalisation'
# -> He tried both and got better results with 'Normalisation'
# -> This was due to using multiple sigmoid functions which require values between 0-1
# -> After these 3 lines all the data values will be btwn 0 & 1
from sklearn.preprocessing import MinMaxScaler  # import the class
sc = MinMaxScaler()                             # create an object of the class with default input
training_set = sc.fit_transform(training_set)   # modify training set by fitting and transforming
## from video - slightly different:
#sc = MinMaxScaler(feature_range = (0, 1))      
#training_set_scaled = sc.fit_transform(training_set)

## Getting the inputs and the ouputs ##
# NB! Time-Steps must be correct to avoid over-fitting & nonsense outputs
## creating a data structure with 60 inuts and 1 output:
# -> Got to 60 through intuition, 60 timesteps corresponds to 60 days input for each days output
# -> since there are 20 working days in each month, this looks at previous 3 months to predict each new day

# -> 'x_train' is the stock prices we have at time -> 't'
# -> For each financial day predicted '_train' will contain the 60 previous stock prices
# -> but exclude the last stock price in the training set because we don't 
#    have the output for the last stock price (1258 is last financial day of 2016)
X_train = training_set[0:1257]  # get all stock prices except last one (time -> t)
# -> 'y_train' is the output that we want to predict at time -> 't+1'
# -> 'y_train' contains the stock price of the next financial day
y_train = training_set[1:1258]  # all stock prices shifted by one (time -> t+1)

## Reshaping ##
# -> Before reshaping, 'x_train' has a 2 dimensional array format corresponding to:
# -> [1] = 1257 observations
# -> [2] = 1 feature (stock price at time -> t)
# Reshaping will change this format into a 3 dimensional array
# -> Keeping current 2 dimensions and adding a time_step
# -> Time_step = 1 -> (t+1) - t = 1
# Must be 3 dimensional according to the Keras input requirement (keras website)
X_train = np.reshape(X_train, (1257, 1, 1))

###############################
## Part 2 - Building the RNN ##
###############################

## Importing the Keras libraries and packages ##
from keras.models import Sequential     # Initialise the RNN
from keras.layers import Dense          # Creates the output layer of RNN
from keras.layers import LSTM           # Type of RNN - Long Term Memory (Best)

## Initialising the RNN ##
# -> Regression is to predict the continuous outcome
# -> Classification is to predict a catagorical outcome
regressor = Sequential()                # Create object for RNN model in a sequence of layers

## Adding the input layer and the LSTM layer ##
# -> units = Number of memory units (4 = common practice in LSTM)
# -> activation = Best results with 'Sigmoid' function (could use Hyperbolic Tangent)
# -> input_shape = Number of features going into network (none=any_time_step , 1=feature)
regressor.add(LSTM(units = 4, activation = 'sigmoid', input_shape = (None, 1)))

## Adding the output layer ##
# -> Dense Class - creates an object of the output layer from import 
# -> units = number of neurons in the output layer & dimension of the output 
# -> units = 1 -> the stock price at time[t+1] = 1 dimension
regressor.add(Dense(units = 1))     # All default values & 1 input

## Compiling the RNN ##
# Compiling requires choosing:
#   => An 'optimiser' for stocastic gradient decent
#   => A 'Loss' criterion to measure the error for each observation we're predicting
# -> 'adam' - less memory requirement (but try RMS pro first?)
# -> 'mean_squared_error' - for training with the sum of the squared differences btwn predicted & real stock prices
regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')

## Fitting the RNN to the Training set ##
# -> To fit the 'x_train' (input) & 'y_train' (output) to the model
# -> Chose epochs=200 based on tuning and testing, got best results
regressor.fit(X_train, y_train, batch_size = 32, epochs = 200)

#################################################################
## Part 3 - Making the predictions and visualising the results ##
#################################################################

# Getting the predicted stock price of 2017 ##
# -> Each day can only predict for the next day because we only have 
#    the real stock price for the 1st day Jan. We need 1st Jan to get 2nd Jan
#    1stJan -> 2ndJan, 2ndJan -> 3rdJan...
# -> In practice we'd have to wait for each real day before predicting the next day
"""
inputs = training_set[1237:1258]                    
inputs = np.reshape(inputs, (21, 1, 1))
predictions = regressor.predict(inputs)
predicted_stock_price = sc.inverse_transform(predictions)
"""

# Getting the real stock price of 2017 ##
test_set = pd.read_csv('Google_Stock_Price_Test.csv')                   # Get the real stock price dataset 
real_stock_price = test_set.iloc[:,1:2].values                          # Get all the rows in column 1

inputs = real_stock_price                                               # Use the 
inputs = sc.transform(inputs)                                           # Scale the inputs to match scale used for training
inputs = np.reshape(inputs, (21, 1, 1))                                 # Change to 3 dimensional array
predicted_stock_price = regressor.predict(inputs)                       # give you the predicted price for month of Jan
predicted_stock_price = sc.inverse_transform(predicted_stock_price)     # scale back to original price values

# Visualising the results ##
plt.plot(real_stock_price, color = 'red', label = 'Real Google Stock Price')
plt.plot(predicted_stock_price, color = 'blue', label = 'Predicted Google Stock Price')
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
real_stock_price_train = pd.read_csv('Google_Stock_Price_Train.csv') 
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
plt.plot(real_stock_price_train, color = 'red', label = 'Real Google Stock Price')
plt.plot(predicted_stock_price_train, color = 'blue', label = 'Predicted Google Stock Price')
plt.title('Google Stock Price Prediction')
plt.xlabel('Time')
plt.ylabel('Google Stock Price')
plt.legend()
plt.show()
