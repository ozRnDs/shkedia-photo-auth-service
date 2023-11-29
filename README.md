# shkedia-photo-auth-service

# Overview
The Users DB service for the Shkedia Private Image Cloud project.
It will handle the communication between the entire system and the database that will handle the crypted users db.
This will be CRUD RESTful API based on FastAPI.

## The service actions
### Handle users
PUT /user  
POST /user/{user_id}  
DELETE /user/{user_id}    
GET /user/search?search_field=search_value    
GET /user/{user_id}  

### Handle user's devices
PUT /device  
POST /device/{device_id}  
DELETE /device/{device_id}  
GET /device/search?search_field=search_value  
GET /device/{device_id}  

### Handle user's authentication
POST /login 

[Information about user authentication process using FastAPI](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/)

### Security
UPDATE /rotate_key

# Deploy


# Development
## Environment

## Build
1. Set the parameters for the build
    ```bash
    export IMAGE_VERSION=cz version -p
    export IMAGE_NAME=shkedia-photo-auth-service:${IMAGE_VERSION}
    export IMAGE_FULL_NAME=public.ecr.aws/q2n5r5e8/ozrnds/${IMAGE_NAME}
    ```
2. Build the image
    ```bash
    docker build . -t ${IMAGE_FULL_NAME}
    ```
3. Push the image
    ```bash
    docker push ${IMAGE_FULL_NAME}
    ```
    Before pushing the image, make sure you are logged in
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
```bash
apt install postgresql
```
For help about the SQL commands type: *\h*  
For help about the PostgreSQL commands type: *\?*

Useful commands:
- \dt * -> Get all the tables in the database (the * can be replaces with any other search parameter)
