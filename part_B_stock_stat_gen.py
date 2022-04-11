import pandas_datareader.data as web
import datetime
import pandas as pd

pd.set_option('display.max_rows', 40)
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 1000)
fiveYearAgo = datetime.datetime(2017, 4, 8)
thisYear = datetime.datetime(2022, 1, 1)
today = datetime.datetime(2022, 4, 8)


def cal_percentage_return(stock):
    return round(((stock['Adj Close'].tail(1).item() / stock['Adj Close'].head(1).item()) - 1.0) * 100, 2)


def cal_max_return_5y(stock5y):
    stock5y_mr = round(((stock5y['Adj Close'].max() / stock5y['Adj Close'].head(1).item()) - 1.0) * 100, 2)
    return stock5y_mr


def cal_mdd_5y(stock5y):
    roll_max = stock5y['Adj Close'].cummax()
    daily_draw_down = stock5y['Adj Close'] / roll_max - 1.0
    max_draw_down = daily_draw_down.cummin()
    return round(max_draw_down.tail(1).item() * 100, 2)


def load_ticker(stock_ticker):
    stock_ytd = web.DataReader(stock_ticker, "yahoo", thisYear, today)
    stock5y = web.DataReader(stock_ticker, "yahoo", fiveYearAgo, today)
    stock_ytd_return_percentage = cal_percentage_return(stock_ytd)
    stock5y_return_percentage = cal_percentage_return(stock5y)
    stock_max_return_5y = cal_max_return_5y(stock5y)
    stock_mdd_5y = cal_mdd_5y(stock5y)
    stock_stat = {
        "Ticker": [stock_ticker],
        "YTD Return": [stock_ytd_return_percentage],
        "5 Year Return": [stock5y_return_percentage],
        "Max Return(5Year)": [stock_max_return_5y],
        "Max Drawdown(5Year)": [stock_mdd_5y],
        "Weighed Score": [round(
            stock_ytd_return_percentage * 15 + stock5y_return_percentage * 5 + stock_max_return_5y * 1 + stock_mdd_5y * 30)]
    }
    return stock_stat


if __name__ == '__main__':
    ticker_input = ""
    while ticker_input != "exit":
        ticker_input = input('Enter the Stock ticker you wanna analyse ( "exit" to exit):')
        if ticker_input != "exit":
            print(load_ticker(ticker_input))

