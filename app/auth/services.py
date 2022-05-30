
from app.auth.models import UserModel


# class AuthServices:

#     @staticmethod
#     def login(username: str, password: str) -> bool:
#         '''
#         Login the user
#         '''
#         #TODO: implement this method
#         raise NotImplementedError()

#     @staticmethod
#     def register(username: str, password: str) -> bool:
#         '''
#         Register the user
#         '''
#         #TODO: implement this method
#         raise NotImplementedError()

class UserServices:

    @staticmethod
    def get_user_by_id(user_id: str) -> UserModel:
        '''
        Get the user by id
        '''
        #TODO: implement this method
        raise NotImplementedError()

    @staticmethod
    def get_user_by_username(username: str) -> UserModel:
        '''
        Get the user by username
        '''
        #TODO: implement this method
        raise NotImplementedError()
    
    @staticmethod
    def add_user_to_db(user: UserModel) -> bool:
        '''
        Add the user to the database 
        '''
        #TODO: implement this method
        raise NotImplementedError()