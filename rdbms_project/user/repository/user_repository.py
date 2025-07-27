from abc import ABC, abstractmethod


class UserRepository(ABC):

    @abstractmethod
    def create_user(self, username, email, hashed_password):
        pass

    @abstractmethod
    def get_user_by_id(self, user_id):
        pass

    @abstractmethod
    def get_user_by_email(self, email):
        pass

    @abstractmethod
    def update_user(self, user_id, username=None, email=None, password=None):
        pass

    @abstractmethod
    def delete_user(self, user_id):
        pass