from pydantic import BaseModel, Field
from uuid import uuid4
from datetime import datetime
from db.service import SqlModel

class User(BaseModel):
    user_id: str = Field(default_factory=lambda: str(uuid4()))
    user_name: str
    created_on: str = Field(default_factory=lambda: datetime.now().isoformat())

class UserDB(User, SqlModel):
    password: str
    
    @staticmethod
    def __sql_create_table__():
        sql_template = """CREATE TABLE users (
            user_id VARCHAR ( 50 ) PRIMARY KEY,
            user_name VARCHAR ( 50 ) UNIQUE NOT NULL,
            password VARCHAR ( 50 ) NOT NULL,
            created_on TIMESTAMP NOT NULL
        )"""
        return sql_template
    
    def __sql_insert__(self):
        sql_template = """INSERT INTO users (
            user_id, user_name, password, created_on
        ) VALUES (%s, %s, %s, %s)"""
        values = (self.user_id, self.user_name, self.password, self.created_on)
        return sql_template, values
    
    @staticmethod
    def __sql_select_item__(field_name, field_value):
        sql_template = f"SELECT * FROM users WHERE {field_name}=%s"
        return sql_template, (field_value,)

    @staticmethod
    def parse_model_from_sql_result(sql_result):
        return User(user_id=sql_result[0],user_name=sql_result[1], password=sql_result[2], created_on=sql_result[3].isoformat())
    
