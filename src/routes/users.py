import logging
logger = logging.getLogger(__name__)
from fastapi import APIRouter, HTTPException
from models.user import UserDB, User
from db.service import DBService

class UserServiceHandler:
    def __init__(self, 
                 db_service: DBService,
                 app_logging_service
                 ):
        self.db_service = db_service
        self.logging_service = app_logging_service
        if not self.db_service.is_ready():
            raise Exception("Can't initializes without repo_service")
        self.router = self.__initialize_routes__()


    def __initialize_routes__(self):
        router = APIRouter(tags=["Users"])
        router.add_api_route(path="", 
                             endpoint=self.post_user,
                             methods=["put"],
                             response_model=User)
        router.add_api_route(path="", 
                             endpoint=self.get_user,
                             methods=["get"],
                             response_model=User)
        router.add_api_route(path="/{user_id}", 
                             endpoint=self.delete_user,
                             methods=["delete"])
        router.add_api_route(path="/{user_id}", 
                             endpoint=self.update_user,
                             methods=["post"],
                             response_model=User)
        return router


    def post_user(self, user_name: str, password: str) -> User:
        
        try:
            new_user: UserDB = self.db_service.insert(UserDB,user_name=user_name, password=password)
            return new_user.toUser()
        except Exception as err:
            logger.error(err)
            raise HTTPException(status_code=500,detail="Can't create user")

    def get_user(self, search_field: str = "user_name", search_value: str = None):
        try:
            search_dictionary = {search_field: search_value}
            get_user: UserDB = self.db_service.select(UserDB,**search_dictionary)
        except Exception as err:
            logger.error(err)
            raise HTTPException(status_code=500,detail="Server Internal Error")
        if get_user is None:
            raise HTTPException(status_code=404, detail="User was not found")
        return get_user.toUser()


    def delete_user(self, user_id: str):
        try:
            user = self.db_service.select(UserDB, user_id=user_id)
            if not user is None:
                self.db_service.delete(user)
                return True
            raise HTTPException(status_code=404, detail="Can't delete user")
        except Exception as err:
            logger.error(err)
            if type(err)==HTTPException:
                raise err
            raise HTTPException(status_code=500, detail="Can't delete user")
    
    def update_user(self, user_id: str) -> User:
        try:
            self.db_service.update(UserDB, user_id=user_id)
        except Exception as err:
            logger.error(err)
            raise HTTPException(status_code=500, detail="Can't Update User")