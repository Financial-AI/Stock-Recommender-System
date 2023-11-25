
from database.models import Base
from database.seed_helpers import seed_symbols_valid_metadata, seed_recommend_csv_data, seed_nasdaq_stock_db_tables
from sqlalchemy import create_engine

import pymysql

sqlEngine       = create_engine('mysql+pymysql://user:password@127.0.0.1:3306/nasdaq_stock', pool_recycle=3600, pool_size=50, max_overflow=50)
dbConnection    = sqlEngine.connect()

# Bind the engine to the Base class
Base.metadata.bind = sqlEngine

# Drop all tables so we can re-create them if there are any changes
Base.metadata.drop_all(sqlEngine)

# Create all tables defined in the Base class and seed tables with data from CSVs
Base.metadata.create_all(sqlEngine)
seed_symbols_valid_metadata(sqlEngine)
seed_nasdaq_stock_db_tables(sqlEngine)

seed_recommend_csv_data(sqlEngine)

