from abc import abstractmethod, ABC


class CommentRepository(ABC):

    @abstractmethod
    def create_comment(self, user, post, content):
        pass

    @abstractmethod
    def get_comments_by_post(self, post_id):
        pass

    @abstractmethod
    def get_comment_by_id(self, comment_id):
        pass

    @abstractmethod
    def update_comment(self, comment_id, new_content):
        pass

    @abstractmethod
    def delete_comment(self, comment_id):
        pass