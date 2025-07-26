from django.urls import path
from user.controller.user_controller import UserController


urlpatterns = [
    path("register/", UserController.register),
    path("get/", UserController.get_user),
    path("update/", UserController.update_user),
    path("delete/", UserController.delete_user),
]