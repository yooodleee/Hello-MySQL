from abc import abstractmethod, ABC


class PostService(ABC):

    @abstractmethod
    def create_new_post(self, title, content, user_id):
        pass

    @abstractmethod
    def get_posts(self, post_id):
        pass

    @abstractmethod
    def get_post_detail(self, post_id):
        pass

    @abstractmethod
    def update_existing_post(self, post_id, title=None, content=None):
        pass

    @abstractmethod
    def delete_existing_post(self, post_id):
        pass