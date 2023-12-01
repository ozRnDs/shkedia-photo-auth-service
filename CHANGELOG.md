## 0.2.0 (2023-12-01)

### Feat

- **src**: Add support of environment depended sql tables. Update the search infrastructure capabilities - able to search on multiple variable

## 0.1.1 (2023-11-29)

### Fix

- **db.service**: Enable autocommit for the sql connection. Handle EOF error

## 0.1.0 (2023-11-29)

### Feat

- **authentication,routes,config**: Create authenication service that handles all the login and secure selected routes with token
- **routes/devices**: Add routes to the devices
- **routes/user**: Create the user route
- **db/service,models/user,device,session**: Create working db.service that excepts objects that enables integration with sql

### Fix

- **src/db/service**: Add try-catch to execure_sql and close temp_cursor to prevent unplaned transactions lock
- **db/service**: Fix the parsing logic of the sql response

### Refactor

- **main.py**: Connect and activate the auth_service. Adding tables creation while the app start up
- **src/models**: Add IF NOT EXISTS to all the CREATE TABLE statements
- **routes/users**: Refactor the errors order, rename to put_user and get the parameters for that route in the body
- **models/user,models/device**: Add classes for the put requests
- **dev**: Create dev script to test the integration with the postgrep db
- **db,-models**: Create the basic concept of the db and models objects
- **src**: Create the basic template of the project
