from comment.entity.comment import Comment
from comment.repository.comment_repository import CommentRepository


class CommentRepositoryImpl(CommentRepository):
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
    
    def create_comment(self, user, post, content):
        return Comment.objects.create(user=user, post=post, content=content)
    
    def get_comments_by_post(self, post_id):
        return Comment.objects.filter(post_id=post_id).select_related('user').order_by('-created_at')
    
    def get_comment_by_id(self, comment_id):
        return Comment.objects.filter(comment_id=comment_id).first()
    
    def update_comment(self, comment_id, new_content):
        comment = self.get_comment_by_id(comment_id)
        if comment:
            comment.content = new_content
            comment.save()
        return comment
    
    def delete_comment(self, comment_id):
        comment = self.get_comment_by_id(comment_id)
        if comment:
            comment.delete()
        return comment
    