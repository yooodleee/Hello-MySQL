from abc import abstractmethod, ABC


class PostRepository(ABC):

    @abstractmethod
    def create_post(self, title, content, user_id):
        pass

    @abstractmethod
    def get_all_posts(self):
        pass

    @abstractmethod
    def get_post_by_id(self, post_id):
        pass

    @abstractmethod
    def update_post(self, post_id, title=None, content=None):
        pass

    @abstractmethod
    def delete_post(self, post_id):
        pass
    