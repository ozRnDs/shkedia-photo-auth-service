import os
import logging
logging.basicConfig(format='%(asctime)s.%(msecs)05d | %(levelname)s | %(filename)s:%(lineno)d | %(message)s' , datefmt='%FY%T')

class ApplicationConfiguration:

    SQL_HOST: str = "127.0.0.1"
    SQL_PORT: int = 1234
    AUTH_DB_NAME: str = "timer_db"
    AUTH_DB_CREDENTIALS_LOCATION: str = "CHANGE ME"

    RECONNECT_WAIT_TIME: int = 1
    RETRY_NUMBER: int = 10

    # Authentication Configuration values
    IDENTITY_TOKEN_LOCATION: str = "CHANGE ME"
    AUTH_SERVICE_URL: str = "CHANGE ME"

    def __init__(self) -> None:
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.logger.info("Start App")

        self.extract_env_variables()
        

    def extract_env_variables(self):
        for attr, attr_type in self.__annotations__.items():
            try:
                self.__setattr__(attr, (attr_type)(os.environ[attr]))
            except Exception as err:
                self.logger.warning(f"Couldn't find {attr} in environment. Run with default value")
        
app_config = ApplicationConfiguration()