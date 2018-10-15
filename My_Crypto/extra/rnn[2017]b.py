#~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Recurrent Neural Network #
#~~~~~~~~~~~~~~~~~~~~~~~~~~#

## Based on code from the video not the Template provided
## Notes and explanations are in the other version

#################################
## Part 1 - Data Preprocessing ##
#################################

# Importing the libraries
import numpy as np                 # To make the arrays. Only input allowed to NN (as apposed to data-frames)
import matplotlib.pyplot as plt    # Used to visualise the results at the end
import pandas as pd                # To import the dataset and manage them easily

## Importing the training set ##
dataset_train = pd.read_csv('BTC[10_2018]_train.csv') # Get the .csv file
training_set = dataset_train.iloc[:,1:2].values             # Get all lines in column 1

## Apply Feature Scaling ##
# -> Could use either 'Standardisation' or 'Normalisation'
# -> He tried both and got better results with 'Normalisation'
# -> This was due to using multiple sigmoid functions which require values between 0-1
# -> After these 3 lines all the data values will be btwn 0 & 1
from sklearn.preprocessing import MinMaxScaler  # import the class
sc = MinMaxScaler(feature_range = (0, 1))      
training_set_scaled = sc.fit_transform(training_set)

## Getting the inputs and the ouputs ##
# NB! Time-Steps must be correct to avoid over-fitting & nonsense outputs
## creating a data structure with 60 inuts and 1 output:
# -> Got to 60 through intuition, 60 timesteps corresponds to 60 days input for each days output
# -> since there are 20 working days in each month, this looks at previous 3 months to predict each new day

# -> 'x_train' is the stock prices we have at time -> 't'
# -> For each financial day predicted '_train' will contain the 60 previous stock prices
# -> but exclude the last stock price in the training set because we don't 
#    have the output for the last stock price (1258 is last financial day of 2016)
X_train = []  # get all stock prices except last one (time -> t)
y_train = []  # all stock prices shifted by one (time -> t+1)
for i in range(60, 1258):
	X_train.append(training_set_scaled[i-60:i, 0])
	y_train.append(training_set_scaled[i, 0])
X_train, y_train = np.array(X_train), np.array(y_train)


## Reshaping ##
# -> Before reshaping, 'x_train' has a 2 dimensional array format corresponding to:
# -> [1] = 1257 observations
# -> [2] = 1 feature (stock price at time -> t)
# Reshaping will change this format into a 3 dimensional array
# -> Keeping current 2 dimensions and adding a time_step
# -> Time_step = 1 -> (t+1) - t = 1
# Must be 3 dimensional according to the Keras input requirement (keras website)
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

###############################
## Part 2 - Building the RNN ##
###############################

## Stacked LSTM with dropout regularization ##

## Importing the Keras libraries and packages ##
from keras.models import Sequential     # Initialise the RNN
from keras.layers import Dense          # Creates the output layer of RNN
from keras.layers import LSTM           # Type of RNN - Long Term Memory (Best)
from keras.layers import Dropout        # To add dropout rate to the layer stack

## Initialising the RNN ##
# -> Regression is to predict the continuous outcome
# -> Classification is to predict a catagorical outcome
regressor = Sequential()                # Create object for RNN model in a sequence of layers

## Adding the input layer and the LSTM layer ##
# -> units = Number of memory units (neurons) - 50 is high dimensionality / multi-layers (3-5 is too little)
# -> return = True -> means there is another layer after this -> stacked layers (false -> no return)
# -> activation = Best results with 'Sigmoid' function (could use Hyperbolic Tangent)
# -> input_shape = Number of features going into network (none=any_time_step, 1=feature)
regressor.add(LSTM(units = 50, return_sequences = True, input_shape = (X_train.shape[1], 1)))
## Add 2nd layer for Dropout Regularization ##
# -> Specify the dropout rate - rate of neurons to ignore (recommends 20%)
regressor.add(Dropout(0.2))

## Adding a 2nd LSTM and Dropout Regularisation ##
regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))

## Adding a 3rd LSTM and Dropout Regularisation ##
regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))

## Adding a 4th LSTM and Dropout Regularisation ##
# -> Defaule return_sequence is False
regressor.add(LSTM(units = 50))
regressor.add(Dropout(0.2))

## Adding the output layer (Fully connected layer) ##
# -> Dense Class - creates an object of the output layer from import 
# -> units = number of neurons in the output layer & dimension of the output 
# -> units = 1 -> the stock price at time[t+1] = 1 dimension
regressor.add(Dense(units = 1))     # All default values & 1 input

## Compiling the RNN ##
# Compiling requires choosing:
#   => An 'optimiser' for stocastic gradient decent (All Optimizers are listed in Keras docs online)
#   => A 'Loss' criterion to measure the error for each observation we're predicting
# -> 'adam' - less memory requirement (but try RMS prop first?)
# -> 'mean_squared_error' - for training with the sum of the squared differences btwn predicted & real stock prices
regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')

## Fitting the RNN to the Training set ##
# -> To fit the 'x_train' (input) & 'y_train' (output) to the model
# -> Chose epochs based on tuning and testing (started at 10, 50, 100 to see what converges with training set)
regressor.fit(X_train, y_train, epochs = 100, batch_size = 32)

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
dataset_test = pd.read_csv('BTC[10_2018]_test.csv')                         # Get the real stock price dataset 
real_stock_price = dataset_test.iloc[:,1:2].values                          # Get all the rows in column 1

## Get the predicted Price of 2018 ##
# Values must be scaled for the RNN inputs:
# -> Can't scale the test value for concat with training set, as test values are lost
# -> Concatanate the original dataframes imported, which gives us inputs of each prediction 
# -> which is the 60 previous prices at each time 't' & then scale these inputs for the predictions
# -> This allows to scale the input without changing the actual values
dataset_total = pd.concat((dataset_train['Open'], dataset_test['Open']), axis = 0)

## Must check that this line references the correct start/end point!! ##
# 60 previous days before start/last day -> [((2018-03-14) - 60days), ((2018-04-14) - 60days)]
inputs = dataset_total[len(dataset_total) - len(dataset_test) - 60:].values     # need to get to the 1st day of test month - 60 days for each 
inputs = inputs.reshape(-1, 1)      # inputs = np.reshape(inputs, (21, 1, 1))   # Change to 3 dimensional array
inputs = sc.transform(inputs)                                                   # Scale the inputs to match scale used for training

# Create new structure of 60 columns of 60 previous values
X_test = []                                              # 
for i in range(60, 80):                                  # range is now 60 + 31 (60 days + num days in test set)
	X_test.append(inputs[i-60:i, 0])
X_test = np.array(X_test)

# Must be 3 dimensional according to the Keras input requirement
X_test = np.reshape(X_train, (X_test.shape[0], X_test.shape[1], 1))	## ValueError: cannot reshape array of size 64860 into shape (31,60,1)

# 
predicted_stock_price = regressor.predict(X_test)                       # give you the predicted price for month of Jan
predicted_stock_price = sc.inverse_transform(predicted_stock_price)     # scale back to original price values

# Visualising the results ##
plt.plot(real_stock_price, color = 'red', label = 'Real BTC Price')
plt.plot(predicted_stock_price, color = 'blue', label = 'Predicted BTC Price')
plt.title('BTC Price Prediction')
plt.xlabel('Time')
plt.ylabel('BTC Price')
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
real_stock_price_train = pd.read_csv('BTC[10_2018]_train.csv') 
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
plt.plot(predicted_stock_price_train, color = 'blue', label = 'Predicted BTC Price')
plt.title('BTC Price Prediction')
plt.xlabel('Time')
plt.ylabel('BTC Price')
plt.legend()
plt.show()
