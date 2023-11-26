from pydantic import BaseModel
from uuid import uuid4
from datetime import datetime
from db.service import SqlModel

class User(BaseModel, SqlModel):
    user_id: str = str(uuid4())
    user_name: str
    password: str
    created_on: str = datetime.now().isoformat()

    @staticmethod
    def __init_model_sql__():
        sql_template = """CREATE TABLE users (
            user_id VARCHAR ( 50 ) PRIMARY KEY,
            user_name VARCHAR ( 50 ) UNIQUE NOT NULL,
            password VARCHAR ( 50 ) NOT NULL,
            created_on TIMESTAMP NOT NULL
        )"""
        return sql_template
    
    def __create_model_sql__(self):
        sql_template = """INSERT INTO users (
            user_id, user_name, password, created_on
        ) VALUES (%s, %s, %s, %s)"""
        values = (self.user_id, self.user_name, self.password, self.created_on)
        return sql_template, values

    def __str__(self) -> str:
        return f"User {self.user_name} is with id: {self.user_id}"

    @staticmethod
    def __get_model_by_field__(field_name, value):
        sql_template = f"SELECT * FROM users WHERE {field_name}=%s"
        return sql_template, (value,)

    @staticmethod
    def parse_model_from_sql_result(sql_result):
        return User(user_id=sql_result[0],user_name=sql_result[1], password=sql_result[2], created_on=sql_result[3].isoformat())
    
