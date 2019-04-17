

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
## Get the real BTC Stock Price of 2012 - 2016 ##
####################################################
## Importing the training set ##
real_stock_price_train = pd.read_csv('BTC[10_2018]_test.csv') 
real_stock_price_train = real_stock_price_train.iloc[:,1:2].values


#########################################################
## Get the predicted BTC Stock Price of 2012 - 2016 ##
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