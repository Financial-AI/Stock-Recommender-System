from typing import Optional, List
from database.models import Base
import sqlalchemy
import pymysql

# sqlEngine       = sqlalchemy.create_engine('mysql+pymysql://user:password@127.0.0.1:3306/nasdaq_stock', pool_recycle=3600, pool_size=50, max_overflow=50)
# dbConnection    = sqlEngine.connect()

# # Bind the engine to the Base class
# Base.metadata.bind = sqlEngine

# # Create all tables defined in the Base class which includes YourModelClass
# Base.metadata.create_all(sqlEngine)

class SQLPipeline:
    def __init__(self):
        """
        ENV MYSQL_USER=mystock_docker
        ENV MYSQL_PASSWORD=mystock_docker
        ENV MYSQL_DATABASE=NASDAQStock
        """
        self.indices_ = ["NASDAQ"]
        self.user_ = "root"
        self.password_ = "stock_autobots"

        # self.user_ = "user"
        # self.password_ = "password"

        self.domain_ = "localhost"
        self.port_ = "3306"
        pymysql.install_as_MySQLdb()

    def create_sqlengine(self, stock_index):
        self.engine_ = sqlalchemy.create_engine(
            f"mysql+pymysql://{self.user_}:{self.password_}@{self.domain_}:{self.port_}/{stock_index}"
        )
        return self.engine_

    def create_sqlconnection(self):
        try:
            self.db_connection_ = self.engine_.connect()
            print(f"self.db_connection_ = {self.db_connection_}")
        except Exception as e:
            print("create_sqlconnection - Connection failed:", e)

    def create_database(self, stock_index):
        # NOTE: No longer works being able to create schema "Database" using engine, it doesnt have execute(...)
        # f"mysql://{self.user_}:{self.password_}@{self.domain_}:{self.port_}/{stock_index}"
        # engine = sqlalchemy.create_engine(
        #     f"mysql://{self.user_}:{self.password_}@{self.domain_}:{self.port_}/"
        # )
        # with self.engine_.connect() as connection:
        self.db_connection_.execute(sqlalchemy.text("CREATE DATABASE nasdaq_stock"))
            # connection.execute(sqlalchemy.schema.CreateSchema(stock_index))
        self.show_databases()


    def show_databases(self):
        # try:
        #     with self.engine_.connect() as connection:
        result = self.db_connection_.execute(sqlalchemy.text("SHOW DATABASES"))
        databases = result.fetchall()
        print("Databases:", databases)
        # except Exception as e:
        #     print("Connection failed:", e)

    def read_stock_metadata(self, url, idx):
        nasdaq = pd.read_html(url)[idx]
        return nasdaq

sql_pipeline = SQLPipeline()

stock_index = "nasdaq_stock"

sql_pipeline.create_sqlengine(stock_index)
sql_pipeline.create_sqlconnection()
# sql_pipeline.create_database(stock_index)
sql_pipeline.show_databases()


