from enum import Enum

class UserType(Enum):
    USER = "fd3f8baa-3ceb-4325-b6d3-72f78b4911fc"
    AGENT = "19455575-0dc5-4209-ab73-85fb008fc25e"
    STAKEHOLDER = "f9f8b9f6-f8f8-4f8f-8f8f-8f8f8f8f8f8f"

class UserModel:

    user_id: str
    username: str
    user_type: UserType
    password: str

    def __init__(self, user_id:str, username:str, user_type:UserType, password:str):
        self.user_id= user_id
        self.username= username
        self.user_type= user_type
        self.password= password

    @staticmethod
    def from_json(json:dict) :
        '''
        Create a UserModel from a json
        '''
        #TODO: implement this method
        raise NotImplementedError()
        

    def to_json(self) -> dict:
        '''
        Create a json from a UserModel
        '''
        #TODO: implement this method
        raise NotImplementedError()