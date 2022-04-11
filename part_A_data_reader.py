import pandas_datareader.data as web
import datetime
import pandas as pd
# formatting the display of dataframe
pd.set_option('display.max_rows', 40)
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 1000)

fiveYearAgo = datetime.datetime(2017, 4, 8)
thisYear = datetime.datetime(2022, 1, 1)
today = datetime.datetime(2022, 4, 8)

# 5 Year Data
tsla5y = web.DataReader("TSLA", "yahoo", fiveYearAgo, today)
print(tsla5y)
print(tsla5y['Adj Close'])

# year-to-date
tslaYTD = web.DataReader("TSLA", "yahoo", thisYear, today)
print(tslaYTD['Adj Close'])

# create new column to store the percentage change
tslaYTD['YTD Return'] = tslaYTD['Adj Close'] / tslaYTD['Adj Close'][0]
print(tslaYTD['YTD Return'])

# tail(1) get the last row, head(1) get the first row,item() return the value stored, round() to limit result to 2dp
tslaYTDReturnPercentage = round((tslaYTD['YTD Return'].tail(1).item() / tslaYTD['YTD Return'].head(1).item() - 1) * 100, 2)
print(tslaYTDReturnPercentage)

print(tsla5y['Adj Close'].tail(1).item())  # last price
print(tsla5y['Adj Close'].head(1).item())  # first price
# to get 5y percentage return of Tesla
tsla5yReturnPercentage = round(((tsla5y['Adj Close'].tail(1).item() / tsla5y['Adj Close'].head(1).item()) - 1.0) * 100, 2)
print(tsla5yReturnPercentage)

print(tsla5y['Adj Close'].max())

# find max return - use the max price occurred in the time period to calculate the percentage
tsla5yMR = round(((tsla5y['Adj Close'].max() / tsla5y['Adj Close'].head(1).item()) - 1.0) * 100, 2)
print(tsla5yMR)

# find MDD
roll_max = tsla5y['Adj Close'].cummax()
print(roll_max)
daily_draw_down = tsla5y['Adj Close']/roll_max - 1.0
print(daily_draw_down)
max_draw_down = daily_draw_down.cummin()
print(max_draw_down)
print(round(max_draw_down.tail(1).item() * 100, 2))

