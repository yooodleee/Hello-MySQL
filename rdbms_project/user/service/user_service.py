from abc import abstractmethod, ABC


class UserService(ABC):

    @abstractmethod
    def register_user(self, username, email, raw_password):
        pass

    @abstractmethod
    def find_user_by_id(self, user_id):
        pass

    @abstractmethod
    def find_user_by_email(self, email):
        pass

    @abstractmethod
    def update_user(self, user_id, username=None, email=None, password=None):
        pass

    @abstractmethod
    def remove_user(self, user_id):
        pass