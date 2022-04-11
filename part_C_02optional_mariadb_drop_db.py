import sqlalchemy
import mariadb

# connect to database
engine = sqlalchemy.create_engine("mariadb+mariadbconnector://root:password@localhost:3306")

# Drop the database( given it exists )
engine.execute("DROP DATABASE stock_analysis")



