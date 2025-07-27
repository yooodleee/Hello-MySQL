from post.entity.post import Post
from user.entity.user import User
from post.repository.post_repository import PostRepository


class PostRepositoryImpl(PostRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        
        return cls.__instance
    
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        
        return cls.__instance
    
    def create_post(self, title, content, user_id):
        user = User.objects.get(user_id=user_id)
        post = Post.objects.create(title=title, content=content, user=user)
        return post
    
    def get_all_posts(self):
        return Post.objects.select_related('user').all()
    
    def get_post_by_id(self, post_id):               
        return Post.objects.select_related('user').get(post_id=post_id)
    
    def update_post(self, post_id, title=None, content=None):
        post = Post.objects.get(post_id=post_id)
        if title:
            post.title = title
        if content:
            post.content = content
        post.save()
        return post
    
    def delete_post(self, post_id):
        post = Post.objects.get(post_id=post_id)
        post.delete()