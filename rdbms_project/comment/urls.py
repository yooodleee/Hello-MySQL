from django.urls import path
from comment.controller.comment_controller import CommentController


urlpatterns = [
    path('create/', CommentController.create_comment),
    path('post/<int:post_id>/', CommentController.list_comments),
    path('update/<int:comment_id>/', CommentController.update_comment),
    path('delete/<int:comment_id>/', CommentController.delete_comment),
]
