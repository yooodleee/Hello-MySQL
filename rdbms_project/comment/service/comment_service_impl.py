from comment.repository.comment_repository_impl import CommentRepositoryImpl
from comment.service.comment_service import CommentService
from post.entity.post import Post
from user.entity.user import User


class CommentServiceImpl(CommentService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__commentRepository = CommentRepositoryImpl.getInstance()
        
        return cls.__instance
    
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        
        return cls.__instance
    
    def create_comment(self, user_id, post_id, content):
        user = User.objects.get(id=user_id)
        post = Post.objects.get(id=post_id)
        return self.__commentRepository.create_comment(user, post, content)
    
    def get_comments_for_post(self, post_id):
        return self.__commentRepository.get_comments_by_post(post_id)
    
    def update_comment(self, comment_id, content):
        return self.__commentRepository.update_comment(comment_id, content)
    
    def delete_comment(self, comment_id):
        return self.__commentRepository.delete_comment(comment_id)
    
    