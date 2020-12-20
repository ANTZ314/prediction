# Crypto Price Prediction

## Dependencies:  

* theano
* pandas
* numpy
* matplotlib
* sklearn
* scikit-learn
* tensorflow
* keras

**Notes:**

* Primary installs listed at the end of this file 
*  All historical data columns need to be flipped vertically to start with earliest date, down to latest date (how to flip at end of doc)
* _virtual_env:_ workon crypto

---
## stocks

**Selected Tickers:**

Ticker | Name | Complete
--- | --- | ---
TSLA | Tesla 		|x|
QCOM | Qualcom	|x|
MSFT | Microsoft	|.|
FB | Netflix Inc		|.|
NFLX | Amazon Inc	|.|
AMZN | Apple Inc	|.|
GOOG | Alphabet Inc |.|

Quandl Key: EfVSTGzAz3sxDyyG2Tqm
Aplhavantage Key: PBRGXKAUD9LKYI3Z

**Note:** - Needed to sym-link alpha-vantage to virtualenv *crypto* to be able to import package:

	cd ~/.virtualenvs/crypto/lib/python3.6/site-packages/
	ln -s /usr/local/lib/python3.6/dist-packages/alpha_vantage alpha_vantage


* **rnnQCOM.py** - Same basic functionality as the above Crypto version, with adaptations for Stock/Exchange currencies...
* **rnnTSLA.py** - same as above but for Tesla

####API Links:
* [Quandl](https://blog.quandl.com/api-for-stock-data?utm_source=direct&utm_medium=blog&utm_campaign=&utm_content=api-for-stock-data)
* [AlphVantage](https://www.alphavantage.co/documentation/)

####Historical Ticker Data:

* **TESLA:**
	* [YAHOO](https://finance.yahoo.com/quote/TSLA/history?period1=1277769600&period2=1606089600&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true)
	* [Nasdaq](https://www.nasdaq.com/market-activity/stocks/tsla/historical)

* **QUALCOM:**
	* [YAHOO](https://finance.yahoo.com/quote/QCOM/history?p=QCOM)
	* [Nasdaq](https://www.nasdaq.com/market-activity/stocks/qcom/historical)

---
## my_crypto  

__Using Bitstamp data__
[Missing Data](https://www.cryptodatadownload.com/)
[Historical Data](https://za.investing.com/crypto/bitcoin/btc-usd-historical-data?cid=49798)
[Quandl BTC API Codes](https://blog.quandl.com/api-for-bitcoin-data?utm_source=blog-quandl&utm_medium=organic&utm_campaign=&utm_content=(homepage))
[Get Bitcoin CSV Data](https://www.cryptodatadownload.com/)  

* **rnn.py**
	* Gets trainging data 'csv' file and checks the size of column 2 (Opening Price)
	* Using the size of the column it trains the LSTM up to the last value stored
	* Make URL request for yesterdays Bitcoin data and extracts the latest 'Open' value
	* Uses this value as the "real_stock_price" for the prediction method
	* Appends last 'Open' price and new Predicted value to text file
	* Appends last 'Open' value to csv column 2 for tomorrow's prediction/evaluation 
* **rnn[2018] BACKUP1.py** - BTCUSD crypto predictor. Graphs test set over predicted values for 30 days of BTC opening price
* **rnn[2018] BACKUP2.py** - ? (possibly same as above)
* **rnn[2018] BACKUP3.py** - Uses full dataset (no test set removed) to predict one days value (opening price)

---
## test

#### api_crypto:
*Various API's to retrieve crypto data*

* **api1.py** - Downloads Yahoo Financial data and graphs it  
* **api2.py** - Using Quandl to retrieve bitcoin (BITSTAMP) data and then graph the 'Low' values from that data (Can't get **Open** price?)  
* **api3.py** - URL request data retrieval, returns byte type then converts to dictionary and extracts opening bitcoin value
* **api4.py**
	* URL request data retrieval returns byte type then converts to dictionary and extracts opening bitcoin value.
	* Checks for 'open.txt' file. If doesn't exist, creates it and writes to it.
	* If it exists, appends new Opening value with date.
* **api5.py** - All of the above and also appends entire dictionary content to csv file under correct columns

#### api_stock:
*Various API's to retrieve stock data*

* **api1_yahoo.py** - Using Yahoo API to request for Qualcomm/Tesla stock data (*Discontinued*)

* **api2_qcom.py** 
	* Using Quandl & Stock's "Ticker Symbol" to retrieve the stock data and then plot the 'High' values
	* Also prints first & last 3 lines of the data

* **api3_qcom.py** 
	* URL request data retrieval from *Yahoo Finance*
	* Returns and prints date / Close price since beginning of the year

* **api4_quandl.py** - Using Quandl API to request for Qualcomm/Tesla stock data

* **api6_quandl.py**
	* Using *yahoo_fin* package to fetch financial data, extract opening price
	* NOT FETCHING TODAYS DATA, ONLY 2 DAYS AGO???


#### csv:
*Various CSV file control testing*

* **csv_test1.py** - Reads values from column 2, print number of values, append date and 'string' to last row of first 2 columns
* **csv_test2.py**
	* Gets number of rows in column 2 = size
	* Prints specified cell according to [col, row] (Note: Cells start at [0, 0])
	* Gets yesterdays Opening & Direction
	* Indicates Y/N for direction correct
	* Shows Error Rate from yesterday to todays Opening price
* **csv_test3.py** - not sure?

---
## ML_Crypto  
Github prediction project **(untested)**

---
## Additional Notes:

__Flip_Data_Columns:__

* Using LibreOffice Writer
* Hightlight all data (excluding the headings)
* **Data -> Descending**

__Useful Stock Tickers:__

* MSFT - Microsoft
* QCOM - Qualcomm
* TSLA - Tesla
* AAPL - Apple

---
### Possibly Removed Folders??

#### My_Google  
Tested on Google stock price and bitcoin opening price (edited from original - I think)

#### My_BitCoin  
**Edited and tested** - rnn.py example from **udemy** using BTCUSD Test and Training set + post processing graphic visualisation  
3 differnt versions of the actual RNN (best version: **rnn.py?**)

###Dependenies to pip3 install:

 Package | Sub-Packages | Version (2017) | Version (2020)
 ----------- |:-----------------:| ------------------- | -------------------
 theano |  			| 0.8.2		| 0.9.0
	 | six  			| 1.9.0		| 1.9.0
	 | scipy  			| 0.11		| 0.14
	 |  numpy  		| 1.7.1 		| 1.9.1
tensorflow  | 			| 1.0.0 		| 1.2.1
	 | six  			| 1.10.0		| 1.10.0
	 |  wheel  			| 0.26		| 0.26
	 |  setuptools		| setuptools	| xx
keras |  				| 2.0.1		| 2.0.6
	|  theano			| xx |
	|  pyyaml			| xx |
	|  six			| xx |
	|  numpy			| xx |
	|  scipy			| xx |
