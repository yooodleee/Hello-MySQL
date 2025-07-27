from post.repository.post_repository_impl import PostRepositoryImpl
from post.service.post_service import PostService
from user.repository.user_repository_impl import UserRepositoryImpl


class PostServiceImpl(PostService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__postRepository = PostRepositoryImpl.getInstance()
        
        return cls.__instance
    
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        
        return cls.__instance
    
    def create_new_post(self, title, content, user_id):
        user = UserRepositoryImpl.get_user_by_id(user_id)
        if not user:
            raise ValueError("작성자가 존재하지 않습니다.")
        return PostRepositoryImpl.create_post(title, content, user)
    
    def get_posts(self, post_id):
        return PostRepositoryImpl.get_post_by_id(post_id)
    
    def get_post_detail(self, post_id):
        return PostRepositoryImpl.get_post_by_id(post_id)
    
    def update_existing_post(self, post_id, title=None, content=None):
        return PostRepositoryImpl.update_post(post_id, title, content)
    
    def delete_existing_post(self, post_id):
        return PostRepositoryImpl.delete_post(post_id)