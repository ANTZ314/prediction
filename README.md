# Crypto Price Prediction

### Dependencies:  

* pandas
* numpy
* matplotlib
* sklearn
* keras

**Note:**

*  All historical data columns need to be flipped vertically to start with earliest date, down to latest date (how to flip at end of doc)
* _virtual_env:_ workon crypto

---
### my_crypto  

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
### stocks

* **rnnQCOM.py** - Same basic functionality as the above Crypto version, with adaptations for Stock/Exchange currencies...
* **rnnTSLA.py** - same as above but for Tesla

**API Links:**
* [Quandl](https://blog.quandl.com/api-for-stock-data?utm_source=direct&utm_medium=blog&utm_campaign=&utm_content=api-for-stock-data)
* [AlphVantage](https://www.alphavantage.co/documentation/)

---
### TEST

#### crypto_api:
*Various API's to retrieve crypto data*

* **api1.py** - Downloads Yahoo Financial data and graphs it  
* **api2.py** - Using Quandl to retrieve bitcoin (BITSTAMP) data and then graph the 'Low' values from that data (Can't get **Open** price?)  
* **api3.py** - URL request data retrieval, returns byte type then converts to dictionary and extracts opening bitcoin value
* **api4.py**
	* URL request data retrieval returns byte type then converts to dictionary and extracts opening bitcoin value.
	* Checks for 'open.txt' file. If doesn't exist, creates it and writes to it.
	* If it exists, appends new Opening value with date.
* **api5.py** - All of the above and also appends entire dictionary content to csv file under correct columns

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

#### stock_api:
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
---
### ML_Crypto  
Github prediction project **(untested)**

### My_Google  
Tested on Google stock price and bitcoin opening price (edited from original - I think)

### My_BitCoin
**Edited and tested** - rnn.py example from **udemy** using BTCUSD Test and Training set + post processing graphic visualisation  
3 differnt versions of the actual RNN (best version: **rnn.py?**)

_______________________________________
#### Additional Notes:

__Flip_Data_Columns:__

* Using LibreOffice Writer
* Hightlight all data (excluding the headings)
* **Data -> Descending**

__Useful Stock Tickers:__

* MSFT - Microsoft
* QCOM - Qualcomm
* TSLA - Tesla
* AAPL - Apple
