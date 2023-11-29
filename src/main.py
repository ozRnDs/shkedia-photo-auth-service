import sys

from fastapi import FastAPI

import traceback


from config import app_config
from authentication.service import AuthService
from db.service import DBService

from routes.users import UserServiceHandler
from routes.devices import DeviceServiceHandler

from models.user import UserDB
from models.device import Device
from models.session import Session
    
app = FastAPI(description="Rest API Interface for the Auth service")

# Initialize all app services
try:
    db_service = DBService(credential_file_location=app_config.AUTH_DB_CREDENTIALS_LOCATION)
    db_service.create_table(UserDB)
    db_service.create_table(Device)
    db_service.create_table(Session)

except Exception as err:
    app_config.logger.error(f"Failed to initialize the db. {err}")
try:
    auth_service = AuthService(jwt_key_location=app_config.JWT_KEY_LOCATION,
                               db_service=db_service,
                               default_expire_delta_min=app_config.TOKEN_TIME_PERIOD)
    user_service = UserServiceHandler(db_service=db_service, app_logging_service=None, auth_service=auth_service)
    device_service = DeviceServiceHandler(db_service=db_service, app_logging_service=None, auth_service=auth_service)
except Exception as err:
    app_config.logger.error(f"Failed to start service. {err}")
    traceback.print_exc()
# Connect all routes
# Example: app.include_router(new_component.router, prefix="/path")

app.include_router(auth_service.router, prefix="/login")
app.include_router(user_service.router, prefix="/user")
app.include_router(device_service.router, prefix="/device")