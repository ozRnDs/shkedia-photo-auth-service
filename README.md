# shkedia-photo-user-db-service

# Overview
The Users DB service for the Shkedia Private Image Cloud project.
It will handle the communication between the entire system and the database that will handle the crypted users db.
This will be CRUD RESTful API based on FastAPI.

## The service actions
### Handle users
GET /users
GET /user/{user_id}
POST /user
UPDATE /user/{user_id}
DELETE /user/{user_id}

### Handle user's devices
GET /user/{user_id}/devices
GET /user/{user_id}/device/{device_id}
POST /user/{user_id}/device
UPDATE /user/{user_id}/device/{device_id}
DELETE /user/{user_id}/device/{device_id}

### Handle user's authentication
POST /user/{user_id}/login
POST /user/{user_id}/logout
GET /user/{user_id}/token

### Security
UPDATE /rotate_key

# Deploy


# Development
## Environment

## Build

## Test



