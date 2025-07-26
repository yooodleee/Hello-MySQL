from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from user.service.user_service_impl import UserServiceImpl
import json


class UserController:
    __userService = UserServiceImpl.getInstance()

    @csrf_exempt
    def register(request):
        if request.method == "POST":
            data = json.loads(request.body)
            user = UserServiceImpl.register_user(data["username"], data["email"], data["password"])
            return JsonResponse({"user_id": user.user_id, "username": user.username})

    @csrf_exempt
    def get_user(request):
        if request.method == "GET":
            user_id = request.GET.get("user_id")
            email = request.GET.get("email")
            user = UserServiceImpl.find_user_by_id(user_id) if user_id else UserServiceImpl.find_user_by_email(email)
            if not user:
                return JsonResponse({"error": "User not found"}, status=404)
            return JsonResponse({
                "user_id": user.user_id,
                "username": user.username,
                "email": user.email,
                "created_at": user.created_at,
            })

    @csrf_exempt
    def update_user(request):
        if request.method == "PUT":
            data = json.loads(request.body)
            user = UserServiceImpl.update_user(
                user_id=data["user_id"],
                username=data.get("username"),
                email=data.get("email"),
                password=data.get("password"),
            )
            if not user:
                return JsonResponse({"error": "User not found"}, status=404)
            return JsonResponse({"user_id": user.user_id, "updated": True})
    
    @csrf_exempt
    def delete_user(request):
        if request.method == "DELETE":
            data = json.loads(request.body)
            deleted, _ = UserServiceImpl.remove_user(data["user_id"])
            return JsonResponse({"deleted": deleted > 0})