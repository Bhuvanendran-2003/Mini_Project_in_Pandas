import pandas as pd

# We load the Google stock data into a DataFrame
google_stock = pd.read_csv('GOOG.csv',parse_dates=['Date'], index_col='Date')

# We load the Apple stock data into a DataFrame
apple_stock = pd.read_csv('AAPL.csv',parse_dates=['Date'], index_col='Date')
                       
# We load the Amazon stock data into a DataFrame
amazon_stock = pd.read_csv('AMZN.csv',parse_dates=['Date'], index_col='Date')

dates = pd.date_range('2000-01-01', '2016-12-31')
all_stocks = pd.DataFrame(index=dates)
# Change the Adj Close column label to Google
google_stock = google_stock[['Adj Close']].rename(columns={'Adj Close': 'Google'})

# Change the Adj Close column label to Apple
apple_stock = apple_stock[['Adj Close']].rename(columns={'Adj Close': 'Apple'})

# Change the Adj Close column label to Amazon
amazon_stock = amazon_stock[['Adj Close']].rename(columns={'Adj Close': 'Amazon'})
all_stocks = all_stocks.join(google_stock)
all_stocks = all_stocks.join(apple_stock)
all_stocks = all_stocks.join(amazon_stock)
all_stocks = all_stocks.dropna()
rollingMean=google_stock.rolling(150).mean()
#print(all_stocks.median())
#print(all_stocks.std())
#print(all_stocks.corr())

#ploing the data
import matplotlib.pyplot as plt

# We plot the Google stock data
plt.plot(all_stocks['Google'])

# We plot the rolling mean ontop of our Google stock data
plt.plot(rollingMean)
plt.legend(['Google Stock Price', 'Rolling Mean'])
plt.show()