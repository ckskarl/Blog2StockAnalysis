import sqlalchemy
import mariadb

# connect to database
engine = sqlalchemy.create_engine("mariadb+mariadbconnector://root:password@localhost:3306")

# create new data base called stock_analysis
engine.execute("CREATE DATABASE stock_analysis")





