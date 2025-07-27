from django.db import models
from user.entity.user import User


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts') # 작성자
    created_at = models.DateTimeField(auto_now_add=True)     # 생성 시 자동 저장
    updated_at = models.DateTimeField(auto_now=True)         # 수정 시 자동 갱신 

    class Meta:
        db_table = "Post"

    def __str__(self):
        return self.title
    