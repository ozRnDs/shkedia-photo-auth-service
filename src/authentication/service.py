import requests


class AuthService:

    def __init__(self,
                 service_token_location: str,
                 user_service_uri: str) -> None:
            
        self.session_token: str = self.__create_session_token__(service_token_location)
        self.user_service_uri = user_service_uri


    def __connection_handshake__(self):
        #TODO: Create secure connection with the auth service
        requests.post()

    def __create_session_token__(self, service_token_location):
        pass
    
    def auth_request(self, request):
        #TODO: Get user's token and check that is valid with the system's auth service
        return True
        pass