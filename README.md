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
## Local Deployment
1. Set the location of the credentials files on the host:
    ```bash
    export HOST_MOUNT=/secrets/auth_credentials
    export AUTH_SERVICE_VERSION=0.0.1
    ```
1. Create credentials token files as follows:
    ```bash
    # Create the folder to be mounted to the container
    if [ ! -d $HOST_MOUNT ]; then
        sudo mkdir $HOST_MOUNT
        sudo chown $USER $HOST_MOUNT
    fi
    # Create the postgres credentials file:
    export SQL_HOST=<write your sql host>
    export SQL_PORT=<write your sql port>
    export DB_NAME=<write your db name>
    export SQL_USER=<write your sql username>
    export SQL_PASSWORD=<write your SQL_PASSWORD>

    cat << EOT > $HOST_MOUNT/postgres_credentials.json
    '{"host": '${SQL_HOST}', "port": '${SQL_PORT}', "db_name": '${DB_NAME}', "user": '${SQL_USER}', "password": '${SQL_PASSWORD}'}'
    EOT
    # Create the jwt token file:
    openssl rand -hex 32 > $HOST_MOUNT/jwt_token
    ```
1. Create *auth.env* file in .local folder with the service variables:
    ```bash
    export CREDENTIALS_FOLDER_NAME=/temp
    export AUTH_DB_CREDENTIALS_LOCATION=$CREDENTIALS_FOLDER_NAME/postgres_credentials.json
    export JWT_KEY_LOCATION=$CREDENTIALS_FOLDER_NAME/jwt_token
    export TOKEN_TIME_PERIOD=15

    if [ ! -d .local ]; then
        sudo mkdir .local
    fi
    cat << EOT > .local/auth_service.env
    CREDENTIALS_FOLDER_NAME=$CREDENTIALS_FOLDER_NAME
    AUTH_DB_CREDENTIALS_LOCATION=$AUTH_DB_CREDENTIALS_LOCATION
    JWT_KEY_LOCATION=$JWT_KEY_LOCATION
    TOKEN_TIME_PERIOD=$TOKEN_TIME_PERIOD
    EOT
    ```
1. Run the service using compose command:
    ```bash
    docker compose up -d
    ```
1. The env can be override by the following command:
    ```bash
    EXPORT AUTH_ENV=.local/auth_service.env
    docker compose --env-file ${AUTH_ENV} up -d
    ```

# Development
## Environment

## Build
1. Set the parameters for the build
    ```bash
    export IMAGE_VERSION=$(cz version -p)
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
