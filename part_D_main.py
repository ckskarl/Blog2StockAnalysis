import pandas_datareader.data as web
import datetime
import pandas as pd
import part_D_db_operation
#pandas_datareader._utils.RemoteDataError
from pandas_datareader._utils import RemoteDataError

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


if __name__ == '__main__': # tsla
    ticker_input = ""
    while ticker_input != "exit":
        ticker_input = input('\nEnter a valid stock ticker to start analyse'
                             '\n e.g. "tsla to analyse Tesla '
                             '\n OR "print" to list the stock_statistic table (alphabetically)'
                             '\n OR "printmax" to list the stock_statistic table (order by Weighed Score) '
                             '\n OR "maxonly" to list the entry in stock_statistic table '
                             'having the highest Weighed Score'
                             '\n OR "del "+ticker to delete existing entry with corresponding ticker e.g. "del tsla" '
                             '\n OR "exit" to exist the program'
                             '\n    Input:')
        match ticker_input: #adbe
            case "exit":
                exit()
            case "print":
                part_D_db_operation.print_table()
            case "printmax":
                part_D_db_operation.print_table_order_by_score(0)
            case "maxonly":
                part_D_db_operation.print_table_order_by_score(1)
            case _:
                if ticker_input.startswith("del "):   # 'del adbe'
                    part_D_db_operation.delete_row(ticker_input[4::]) # 'adbe'
                else:
                    try:
                        part_D_db_operation.insert_new_row(load_ticker(ticker_input))
                    except RemoteDataError:
                        print("Invalid ticker, please try again")





