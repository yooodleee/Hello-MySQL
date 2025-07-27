from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from user.service.user_service_impl import UserServiceImpl
import json


class UserController(viewsets.ViewSet):
    __userService = UserServiceImpl.getInstance()

    @action(detail=False, methods=["post"])
    def register(self, request):
        data = request.data
        try: 
            user = UserServiceImpl.register_user(
                username=data["username"],
                email=data["email"],
                password=data["password"]
            )
            return Response({"user_id": user.user_id, "username": user.username}, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=["get"])
    def get_user(self, request):
        try:
            user_id = request.GET.get("user_id")
            email = request.GET.get("email")

            service = UserServiceImpl.getInstance()
            user = UserServiceImpl.find_user_by_id(user_id) if user_id else UserServiceImpl.find_user_by_email(email)

            if not user:
                return Response({"error": "사용자를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)
            return Response({
                "user_id": user.user_id,
                "username": user.username,
                "email": user.email,
                "created_at": user.created_at,
            })
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=["put"])
    def update_user(self, request):
        try:
            data = json.loads(request.body)
            user = UserServiceImpl.getInstance().update_user(
                user_id=data["user_id"],
                username=data.get("username"),
                email=data.get("email"),
                password=data.get("password"),
            )
            if not user:
                return Response({"error": "사용자를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        
            return Response({"user_id": user.user_id, "updated": True})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @action(detail=True, methods=["delete"])
    def delete_user(self, request):
        try:
            data = json.loads(request.body)
            deleted, _ = UserServiceImpl.getInstance().remove_user(data["user_id"])
            return Response({"deleted": deleted > 0})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        