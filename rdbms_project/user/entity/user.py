from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    password = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "User"
    
    def __str__(self):
        return self.username