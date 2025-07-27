from django.urls import path
from post.controller.post_controller import PostController


urlpatterns = [
    path('posts/', PostController.list_posts),
    path('posts/create/', PostController.create_post),
    path('posts/<int:post_id>/', PostController.post_detail),
    path('posts/<int:post_id>/update/',PostController.update_post),
    path('posts/<int:post_id>/delete/', PostController.delete_post),
]