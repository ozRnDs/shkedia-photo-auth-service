import sys

from fastapi import FastAPI
import uvicorn


from config import app_config
from authentication.service import AuthService
from db.service import DBService

from routes.users import UserServiceHandler
from routes.devices import DeviceServiceHandler

    
app = FastAPI(description="Rest API Interface for the timer service")

 #TODO: Bind auth service as middleware to all requests

# Initialize all app services
try:
    auth_service = AuthService(service_token_location=app_config.IDENTITY_TOKEN_LOCATION,
                            user_service_uri=app_config.AUTH_SERVICE_URL)
    db_service = DBService(credential_file_location=app_config.AUTH_DB_CREDENTIALS_LOCATION)
    user_service = UserServiceHandler(db_service=db_service, app_logging_service=None)
    device_service = DeviceServiceHandler(db_service=db_service, app_logging_service=None)
except Exception as err:
    app_config.logger.error(f"Failed to start service. {err}")
# Connect all routes
# Example: app.include_router(new_component.router, prefix="/path")

app.include_router(user_service.router, prefix="/user")
app.include_router(device_service.router, prefix="/device")



if __name__ == "__main__":
    pass

    # uvicorn.run("main:app", host="0.0.0.0", port=5000, log_level="info", access_log=False)