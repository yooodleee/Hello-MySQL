from abc import abstractmethod, ABC


class CommentService(ABC):

    @abstractmethod
    def create_comment(self, user_id, post_id, content):
        pass

    @abstractmethod
    def get_comments_for_post(self, post_id):
        pass

    @abstractmethod
    def update_comment(self, comment_id, content):
        pass

    @abstractmethod
    def delete_comment(self, comment_id):
        pass
    