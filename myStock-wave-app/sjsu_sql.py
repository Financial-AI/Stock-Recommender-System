import sqlalchemy
import pymysql

class SQLPipeline:
    def __init__(self):
        self.indices_ = ["NASDAQ"]
        self.user_ = "root"
        self.password_ = "12345678"
        self.domain_ = "localhost"
        self.port_ = "3306"

    def create_schema(self, index):
        engine = sqlalchemy.create_engine(
            f"mysql://{self.user_}:{self.password_}@{self.domain_}:{self.port_}"
        )
        engine.execute(sqlalchemy.schema.CreateSchema(index))

