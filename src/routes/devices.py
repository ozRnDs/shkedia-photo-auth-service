import logging
logger = logging.getLogger(__name__)
from fastapi import APIRouter, HTTPException, Depends
from typing import Union, List

from models.user import UserDB, User
from models.device import Device, DeviceRequest
from db.service import DBService
from authentication.service import AuthService

class DeviceServiceHandler:
    def __init__(self, 
                 db_service: DBService,
                 app_logging_service,
                 auth_service: AuthService
                 ):
        self.db_service = db_service
        self.logging_service = app_logging_service
        self.auth_service = auth_service
        if not self.db_service.is_ready():
            raise Exception("Can't initializes without repo_service")
        self.router = self.__initialize_routes__()


    def __initialize_routes__(self):
        router = APIRouter(tags=["Devices"],
                           dependencies=[Depends(self.auth_service.__get_user_from_token__)])
        router.add_api_route(path="", 
                             endpoint=self.put_device,
                             methods=["put"],
                             response_model=Device)
        router.add_api_route(path="/search", 
                             endpoint=self.search_device,
                             methods=["get"],
                             response_model=Union[Device,List[Device]])
        router.add_api_route(path="/{device_id}", 
                             endpoint=self.get_device,
                             methods=["get"],
                             response_model=Device)
        router.add_api_route(path="/{device_id}", 
                             endpoint=self.delete_device,
                             methods=["delete"])
        router.add_api_route(path="/{device_id}", 
                             endpoint=self.update_device,
                             methods=["post"],
                             response_model=Device)
        return router

    def put_device(self, device: DeviceRequest):
        try:
            user = self.db_service.select(UserDB, user_name=device.owner_name)
            if user is None:
                raise HTTPException(status_code=404, detail="Can't find user")
            new_device = self.db_service.insert(Device, 
                                        device_name=device.device_name,
                                        owner_id=user.user_id)
            return new_device
        except Exception as err:
            if type(err) == HTTPException:
                raise err
            logger.error(err)
            raise HTTPException(status_code=500, detail="Can't create device")

    def get_device(self, device_id: str = None)-> Device:
        return self.search_device(search_field="device_id", search_value=device_id)
    

    def search_device(self, search_field: str = "device_name", search_value: str = None) -> Device:
        try:
            search_dictionary = {search_field: search_value}
            get_device: Device = self.db_service.select(Device,**search_dictionary)
            if get_device is None:
                raise HTTPException(status_code=404, detail="Device was not found")
            return get_device
        except Exception as err:
            if type(err)==HTTPException:
                raise err
            logger.error(str(err))
            raise HTTPException(status_code=500,detail="Server Internal Error")

    def delete_device(self, device_id: str):
        try:
            device = self.db_service.select(Device, device_id=device_id)
            if device is None:
                raise HTTPException(status_code=404, detail="Can't delete device")
            self.db_service.delete(device)
            return True
        except Exception as err:
            if type(err)==HTTPException:
                raise err
            logger.error(err)
            raise HTTPException(status_code=500, detail="Can't delete device")

    def update_device(self, device_id: str) -> Device:
        try:
            self.db_service.update(Device, device_id=device_id)
        except Exception as err:
            logger.error(err)
            raise HTTPException(status_code=500, detail="Can't Update Device")