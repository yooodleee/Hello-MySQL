from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status
import json

from post.service.post_service_impl import PostServiceImpl


class PostController(viewsets.ViewSet):
    __postService = PostServiceImpl.getInstance()

    @action(detail=False, methods=["post"])
    def create_post(self, request):
        data = json.loads(request.body)
        try:
            post = PostServiceImpl.create_new_post(
                title=data["title"],
                content=data["content"],
                user_id=data["user_id"]
            )
            return Response({"id": post.post_id, "message": "게시글 작성 완료"}, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=["get"])
    def list_posts(self, request):
        posts = PostServiceImpl.get_posts()
        data = [{
            "id": p.id,
            "title": p.title,
            "content": p.content,
            "user": {
                "id": p.user.user_id,
                "username": p.user.username,
                "email": p.user.email
            },
            "created_at": p.created_at,
            "updated_at": p.updated_at
        } for p in posts]
        return Response(data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=["get"])
    def post_detail(self, request, post_id):
        post = PostServiceImpl.get_post_detail(post_id)
        if post:
            data = {
                "id": post.id,
                "title": post.title,
                "content": post.content,
                "user": post.user.user_id,
                "created_at": post.created_at,
                "updated_at": post.updated_at
            }
            return Response(data, status=status.HTTP_200_OK)
        return Response({"error": "게시글을 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=True, methods=["put"])
    def update_post(self, request, post_id):
        data = json.loads(request.body)
        post = PostServiceImpl.update_existing_post(
            post_id=post_id,
            title=data["title"],
            content=data["content"]
        )
        if post:
            return Response({"message": "게시글 수정 완료"}, status=status.HTTP_200_OK)
        return ResourceWarning({"error": "게시글이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)
        
    @action(detail=True, methods=["delete"])
    def delete_post(self, request, post_id):
        post = PostServiceImpl.delete_existing_post(post_id)
        if post:
            return Response({"message": "게시글 삭제 완료"}, status=status.HTTP_200_OK)
        return Response({"error": "게시글이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)