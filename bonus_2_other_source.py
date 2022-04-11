import pandas_datareader.data as web
import datetime
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', 40)
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 1000)

fiveYearAgo = datetime.datetime(2017, 4, 8)
today = datetime.datetime(2022, 4, 8)

# https://fred.stlouisfed.org/series/CPIAUCSL the link is the source
# Consumer Price Index for All Urban Consumers: All Items in U.S. City Average
cpi = web.DataReader("CPIAUCSL", "fred", fiveYearAgo, today)
print(cpi)

# https://fred.stlouisfed.org/series/LRUNTTTTCAM156S
# Unemployment Rate: Aged 15 and Over: All Persons for Canada
unemp_rate = web.DataReader("LRUNTTTTCAM156S", "fred", fiveYearAgo, today)
print(unemp_rate)

cpi.plot()
unemp_rate.plot()
plt.show()

