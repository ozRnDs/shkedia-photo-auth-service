import logging
logger = logging.getLogger(__name__)
from fastapi import APIRouter, HTTPException, Depends, status

from typing import Annotated
from models.user import UserDB, User, UserRequest
from db.service import DBService
from authentication.service import AuthService, OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class UserServiceHandler:
    def __init__(self, 
                 db_service: DBService,
                 auth_service: AuthService,
                 app_logging_service
                 ):
        self.db_service = db_service
        self.auth_service = auth_service
        self.logging_service = app_logging_service
        if not self.db_service.is_ready():
            raise Exception("Can't initializes without repo_service")
        self.router = self.__initialize_routes__()


    def __initialize_routes__(self):
        router = APIRouter(tags=["Users"])
        router.add_api_route(path="", 
                             endpoint=self.put_user,
                             methods=["put"],
                             response_model=User,
                             )
        router.add_api_route(path="", 
                             endpoint=self.get_user,
                             methods=["get"],
                             response_model=User,
                             dependencies=[Depends(self.auth_service.__get_user_from_token__)],
                            )
        router.add_api_route(path="/{user_id}", 
                             endpoint=self.delete_user,
                             methods=["delete"],
                             dependencies=[Depends(self.auth_service.__get_user_from_token__)],
                             )
        router.add_api_route(path="", 
                             endpoint=self.update_user,
                             methods=["post"],
                             response_model=User,
                             dependencies=[Depends(self.auth_service.__get_user_from_token__)])
        return router

    def put_user(self, user: UserRequest) -> User:       # current_user: Annotated[UserDB, Depends(AuthService().__get_user_from_token__)]
        try:
            user.password = self.auth_service.get_password_hash(user.password)
            new_user: UserDB = self.db_service.insert(UserDB,**user.model_dump())
            return new_user.toUser()
        except Exception as err:
            logger.error(err)
            raise HTTPException(status_code=500,detail="Can't create user")

    def get_user(self, search_field: str = "user_name", search_value: str = None):
        try:
            search_dictionary = {search_field: [search_value]}
            get_user: UserDB = self.db_service.select(UserDB,**search_dictionary)
        except Exception as err:
            logger.error(err)
            raise HTTPException(status_code=500,detail="Server Internal Error")
        if get_user is None:
            raise HTTPException(status_code=404, detail="User was not found")
        return get_user.toUser()


    def delete_user(self, user_id: str):
        try:
            user = self.db_service.select(UserDB, user_id=[user_id])
            if user is None:
                raise HTTPException(status_code=404, detail="Can't delete user")
            self.db_service.delete(user)
            return True    
        except Exception as err:
            logger.error(err)
            if type(err)==HTTPException:
                raise err
            raise HTTPException(status_code=500, detail="Can't delete user")
    
    def update_user(self, new_user: UserDB) -> User:
        try:
            raise NotImplementedError("I'm not ready for that. In the near future. I promise")
            current_user = self.get_user(search_field="user_id", search_value=new_user.user_id) #TODO: Think about the user update. The password field should be ignored
            self.db_service.update(current_user,new_user)
            return new_user.toUser()
        except Exception as err:
            logger.error(err)
            if type(err)==AttributeError:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))
            raise HTTPException(status_code=500, detail="Can't Update User")