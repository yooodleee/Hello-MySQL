from abc import abstractmethod, ABC


class UserService(ABC):

    @abstractmethod
    def register_user(username, email, raw_password):
        pass

    @abstractmethod
    def find_user_by_id(user_id):
        pass

    @abstractmethod
    def find_user_by_email(email):
        pass

    @abstractmethod
    def update_user(user_id, username=None, email=None, password=None):
        pass

    @abstractmethod
    def remove_user(user_id):
        pass