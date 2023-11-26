from config import app_config

from fastapi import FastAPI
import uvicorn

from authentication.service import AuthService

app = FastAPI(description="Rest API Interface for the timer service")


# Initialize all app services
auth_service = AuthService(service_token_location=app_config.IDENTITY_TOKEN_LOCATION,
                           user_service_uri=app_config.AUTH_SERVICE_URL)




 #TODO: Bind auth service as middleware to all requests

# Connect all routes
# Example: app.include_router(new_component.router, prefix="/path")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, log_level="info", access_log=False)