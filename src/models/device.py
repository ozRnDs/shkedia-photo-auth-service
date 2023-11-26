from pydantic import BaseModel
from typing import Union
from uuid import uuid4
from datetime import datetime

from db.service import SqlModel

class Device(BaseModel, SqlModel):
    device_id: str = str(uuid4())
    device_name: str
    owner_id: str
    created_on: str = datetime.now().isoformat()
    status: str = "ACTIVE"

    @staticmethod
    def __init_model_sql__():
        sql_template = """CREATE TABLE devices (
            device_id VARCHAR ( 50 ) PRIMARY KEY,
            device_name VARCHAR ( 50 ) UNIQUE NOT NULL,
            owner_id VARCHAR ( 50 ) NOT NULL REFERENCES users(user_id),
            created_on TIMESTAMP NOT NULL,
            device_status VARCHAR ( 50 )
        )"""
        return sql_template
    
    def __create_model_sql__(self):
        sql_template = """INSERT INTO devices (
            device_id, device_name, owner_id, created_on, device_status
        ) VALUES (%s, %s, %s, %s, %s)"""
        values = (self.device_id, self.device_name, self.owner_id, self.created_on, self.status)
        return sql_template, values

    # @staticmethod
    # def create_user(user_name: str, password: str):
    #     new_user = User(user_name=user_name, password=password)
    #     return new_user

    
