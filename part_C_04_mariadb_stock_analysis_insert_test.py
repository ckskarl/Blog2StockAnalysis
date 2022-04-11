import pandas as pd
import sqlalchemy
import mariadb
pd.set_option('display.max_rows', 40)
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 1000)

from sqlalchemy import Table, Column, Integer, String, MetaData, Float

# connect to database
engine = sqlalchemy.create_engine("mariadb+mariadbconnector://root:password@localhost:3306/stock_analysis", echo=True)

test_data = {
    "Ticker": ['test'],
    "YTD Return": [1.0],
    "5 Year Return": [2.0],
    "Max Return(5Year)": [3.0],
    "Max Drawdown(5Year)": [4.0],
    "Weighed Score": [5.0]
}

test_data_df = pd.DataFrame.from_dict(test_data)
test_data_df.to_sql('stock_statistic', con=engine, if_exists='append', chunksize=1000, index=False)
print(pd.read_sql("SELECT * FROM stock_statistic", con=engine))


