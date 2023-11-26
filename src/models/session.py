from pydantic import BaseModel
from typing import Union
from uuid import uuid4
from datetime import datetime, timedelta

from db.service import SqlModel

class Session(BaseModel, SqlModel):
    session_id: str = str(uuid4())
    user_id: str
    device_id: str
    session_secret: str
    expiration_date: str = (datetime.now() + timedelta(days=7)).isoformat()
    last_activity: Union[str, None] = None

    @staticmethod
    def __init_model_sql__():
        sql_template = """CREATE TABLE sessions (
            session_id VARCHAR ( 50 ) PRIMARY KEY,
            user_id VARCHAR ( 50 ) NOT NULL REFERENCES users(user_id),
            device_id VARCHAR ( 50 ) NOT NULL REFERENCES devices(device_id),
            session_secret VARCHAR ( 50 ) UNIQUE NOT NULL,
            expiration_date TIMESTAMP NOT NULL,
            last_activity TIMESTAMP
        )"""
        return sql_template
    
    def __create_model_sql__(self):
        sql_template = """INSERT INTO sessions (
            session_id, user_id, device_id, session_secret, expiration_date, last_activity
        ) VALUES (%s, %s, %s, %s, %s, %s)"""
        values = (self.session_id, self.user_id, self.device_id, self.session_secret, self.expiration_date, self.last_activity)
        return sql_template, values

    # @staticmethod
    # def create_user(user_name: str, password: str):
    #     new_user = User(user_name=user_name, password=password)
    #     return new_user

    
