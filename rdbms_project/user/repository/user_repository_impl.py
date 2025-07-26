from user.entity.user import User
from user.repository.user_repository import UserRepository
from django.core.exceptions import ObjectDoesNotExist


class UserRepositoryImpl(UserRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        
        return cls.__instance
    
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

    def create_user(username, email, hashed_password):
        return User.objects.create(username=username, email=email, password=hashed_password)
    
    def get_user_by_id(user_id):
        return User.objects.filter(user_id=user_id).first()
    
    def get_user_by_email(email):
        return User.objects.filter(email=email).first()
    
    def update_user(user_id, username=None, email=None, password=None):
        try:
            user = User.objects.get(user_id=user_id)
            if username:
                user.username = username
            if email:
                user.email = email
            if password:
                user.password = password
            user.save()
            return user
        except ObjectDoesNotExist:
            return None
    
    def delete_user(user_id):
        return User.objects.filter(user_id=user_id).delete()