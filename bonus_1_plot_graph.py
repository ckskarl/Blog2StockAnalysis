import pandas_datareader.data as web
import datetime
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', 40)
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 1000)
fiveYearAgo = datetime.datetime(2017, 4, 8)
today = datetime.datetime(2022, 4, 8)

tsla5y = web.DataReader("TSLA", "yahoo", fiveYearAgo, today)


tsla5y['Adj Close'].plot(figsize=(32, 9))
plt.title('Tesla Stock Price')
plt.ylabel('Adjusted Closing Price')
plt.grid(color='grey', linestyle='--', linewidth=0.5)
plt.show()

