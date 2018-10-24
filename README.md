# Crypto Price Prediction

### Dependencies:  

* pandas
* numpy
* matplotlib
* sklearn
* keras

[Quandl BTC API Codes](https://blog.quandl.com/api-for-bitcoin-data?utm_source=blog-quandl&utm_medium=organic&utm_campaign=&utm_content=(homepage))



#### Docs  
Various documents related to RNN's, LSTM's and stock prediction

#### Google_Original
Orignal example from **udemy** using Google Stock Prices

#### Homework  
RNN error calculation and accuracy analysis.
Fine tuning algorithm 

#### My_Crypto  

* **rnn[2018].py**
	* Gets trainging data 'csv' file and checks the size of column 2 (Opening Price)
	* Using the size of the column it trains the LSTM up to the last value stored
	* Make URL request for yesterdays Bitcoin data and extracts the latest 'Open' value
	* Uses this value as the "real_stock_price" for the prediction method
	* Print predicted value to text file and append to column 2 for tomorrows evaluation 
* **rnn[2018] BACKUP1.py** - BTCUSD crypto predictor. Graphs test set over predicted values for 30 days of BTC opening price
* **rnn[2018] BACKUP2.py** - ?
* **rnn[2018] BACKUP3.py** - Uses full dataset (no test set removed) to predict one days value (opening price)

#### API  

* **api1.py** - Downloads Yahoo Financial data and graphs it  
* **api2.py** - Using Quandl to retrieve bitcoin (BITSTAMP) data and then graph the 'Low' values from that data (Can't get **Open** price?)  
* **api3.py** - URL request data retrieval, returns byte type then converts to dictionary and extracts opening bitcoin value
* **api4.py**
	* URL request data retrieval returns byte type then converts to dictionary and extracts opening bitcoin value.
	* Checks for 'open.txt' file. If doesn't exist, creates it and writes to it.
	* If it exists, appends new Opening value with date.

#### ML_BTC  
2x BTC market value '.csv' files in USD + **rnnQuick.py**

#### ML_Crypto  
Github prediction project **(untested)**

#### My_Google  
Tested on Google stock price and bitcoin opening price (edited from original - I think)

#### My_BitCoin
**Edited and tested** - rnn.py example from **udemy** using BTCUSD Test and Training set + post processing graphic visualisation  
3 differnt versions of the actual RNN (best version: **rnn.py?**)