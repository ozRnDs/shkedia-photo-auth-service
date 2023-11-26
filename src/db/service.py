import logging
logger = logging.getLogger(__name__)
import json
import psycopg
from abc import ABC

from db.sql_from_model import get_table_name_from_object

class SqlModel(ABC):

    @staticmethod
    def __init_model_sql__():
        pass

    def __create_sql_model__(self):
        pass

    def __does_table_exists__(self):
        table_name = get_table_name_from_object(self)
        sql_template = ...
        return ...


class DBService:

    def __init__(self,
                 credential_file_location: str,
                 connection_timeout: int=10
                 ) -> None:
        self.credential_file_location = credential_file_location
        credential_object = self.__get_credentials_from_file__()
        try:
            self.db_connection_object = psycopg.connect(host=credential_object["host"],
                                                        port=credential_object["port"],
                                                        dbname=credential_object["db_name"],
                                                        user=credential_object["user"],
                                                        password=credential_object["password"],
                                                        connect_timeout=connection_timeout)
        except Exception as err:
            logger.error(err)
        if self.db_connection_object.closed:
            raise ConnectionError("Couldn't connect to the server")
    
    def __get_credentials_from_file__(self):
        with open(self.credential_file_location, 'r') as file:
            credential_object = json.load(file)
        return credential_object

    def insert_object(self, model_object: SqlModel):
        sql_template, values = model_object.__create_sql_model__()
        self.execute_sql(sql_template=sql_template, values=values)

    def execute_sql(self, sql_template, values: tuple):
        response=None
        temp_curser = self.db_connection_object.cursor()
        temp_curser.execute(sql_template, values)
        if self.__is_changing_query__(sql_template):
            self.db_connection_object.commit()
        if "SELECT" in temp_curser.statusmessage:
            response = temp_curser.fetchall()
        temp_curser.close()
        return response

    def __is_changing_query__(self, query):
        if "INSERT INTO" in query:
            return True
        if "UPDATE" in query:
            return True
        if "CREATE" in query:
            return True
        if "DROP" in query:
            return True

    def __del__(self):
        self.close()

    def close(self):
        if not self.db_connection_object:
            return
        if self.db_connection_object.closed:
            return
        self.db_connection_object.close()

        
