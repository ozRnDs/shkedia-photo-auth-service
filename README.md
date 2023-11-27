# shkedia-photo-auth-service

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

[Information about user authentication process using FastAPI](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/)

### Security
UPDATE /rotate_key

# Deploy


# Development
## Environment

## Build

## Test

## Basic CLI command for PostgreSql
### Bash CLI
1. Connecting to the Server:
    ```bash
    export HOST_ENDPOINT=<Your DB Endpoint> # In aws usually: <db_instance_name>.<region>.rds.amazonaws.com
    export USER=<Your DB User name>
    export DBNAME=<Yourdb Name>

    psql -h $HOST_ENDPOINT -U $USER -d $DBNAME
    ```
### psql CLI
In the psql itself you can write SQLs and use the PostgreSQL syntax for more options.  
For help about the SQL commands type: *\h*  
For help about the PostgreSQL commands type: *\?*

Useful commands:
- \dt * -> Get all the tables in the database (the * can be replaces with any other search parameter)
