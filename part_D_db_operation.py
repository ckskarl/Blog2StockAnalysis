import pandas as pd
import sqlalchemy
import mariadb
from sqlalchemy.exc import IntegrityError
#sqlalchemy.exc.IntegrityError:
pd.set_option('display.max_rows', 40)
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 1000)

# connect to database
engine = sqlalchemy.create_engine("mariadb+mariadbconnector://root:password@localhost:3306/stock_analysis")


def print_table():
    print(pd.read_sql("SELECT * FROM stock_statistic", con=engine))


def print_table_order_by_score(mode):
    if mode == 0:
        print(pd.read_sql("SELECT * FROM stock_statistic order by 6 desc", con=engine))
    elif mode == 1:
        print(pd.read_sql("SELECT * FROM stock_statistic order by 6 desc LIMIT 1", con=engine))


def insert_new_row(ticker_dict):
    data_df = pd.DataFrame.from_dict(ticker_dict)
    try:
        data_df.to_sql('stock_statistic', con=engine, if_exists='append', chunksize=1000, index=False)
        print(ticker_dict)
        print("It has bee added to the table.")
    except IntegrityError:
        print("The stock statistic is already in the table! Please enter another ticker value.")


def delete_row(ticker):
    print("Searching for  '"+ticker+"' in the table...")
    if engine.execute("DELETE FROM stock_statistic WHERE Ticker = '"+ticker+"'").rowcount > 0:
        print("Entry deleted")
    else:
        print("No matching result, no entry is deleted")

