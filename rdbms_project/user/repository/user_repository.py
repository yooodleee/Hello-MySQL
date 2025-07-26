from abc import ABC, abstractmethod


class UserRepository(ABC):

    @abstractmethod
    def create_user(username, email, hashed_password):
        pass

    @abstractmethod
    def get_user_by_id(user_id):
        pass

    @abstractmethod
    def get_user_by_email(email):
        pass

    @abstractmethod
    def update_user(user_id, username=None, email=None, password=None):
        pass

    @abstractmethod
    def delete_user(user_id):
        pass