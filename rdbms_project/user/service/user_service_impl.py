from user.repository.user_repository_impl import UserRepositoryImpl
from user.service.user_service import UserService
from django.contrib.auth.hashers import make_password, check_password


class UserServiceImpl(UserService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__userRepository = UserRepositoryImpl.getInstance()
        
        return cls.__instance
    
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        
        return cls.__instance
    
    def register_user(self, username, email, raw_password):
        hashed_pw = make_password(raw_password)
        return UserRepositoryImpl.create_user(username, email, hashed_pw)
    
    def find_user_by_id(self, user_id):
        return UserRepositoryImpl.get_user_by_id(user_id)
    
    def find_user_by_email(self, email):
        return UserRepositoryImpl.get_user_by_email(email)
    
    def update_user(self, user_id, username=None, email=None, password=None):
        hashed_pw = make_password(password) if password else None
        return UserRepositoryImpl.update_user(user_id, username, email, hashed_pw)
    
    def remove_user(self, user_id):
        return UserRepositoryImpl.delete_user(user_id)