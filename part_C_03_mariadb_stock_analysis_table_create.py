import pandas as pd
import sqlalchemy
import mariadb
from sqlalchemy import Table, Column, Integer, String, MetaData, Float

# connect to database
engine = sqlalchemy.create_engine("mariadb+mariadbconnector://root:password@localhost:3306/stock_analysis", echo=True)

meta = MetaData()

stock_stat = Table(
    'stock_statistic', meta,
    Column('Ticker', String(10), primary_key=True),
    Column('YTD Return', Float),
    Column('5 Year Return', Float),
    Column('Max Return(5Year)', Float),
    Column('Max Drawdown(5Year)', Float),
    Column('Weighed Score', Float)
)

meta.create_all(engine)

# read table and turn it into DataFrame type
table_df = pd.read_sql_table('stock_statistic', con=engine)
table_df.info()

