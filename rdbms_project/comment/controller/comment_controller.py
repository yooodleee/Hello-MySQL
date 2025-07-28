from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status
import json

from comment.service.comment_service_impl import CommentServiceImpl


class CommentController(viewsets.ViewSet):
    __commentService = CommentServiceImpl.getInstance()

    @action(detail=False, methods=["post"])
    def create_comment(self, request):
        data = json.loads(request.body)
        comment = self.__commentService.create_comment(
            user_id=data['user_id'],
            post_id=data['post_id'],
            content=data['content']
        )
        return Response({'id': comment.comment_id, 'message': '댓글이 생성되었습니다.'}, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['get'])
    def list_comments(self, request, post_id):
        comments = self.__commentService.get_comments_for_post(post_id)
        results = [
            {
                'id': c.comment_id,
                'content': c.content,
                'user_id': c.user.id,
                'username': c.user.username,
                'created_at': c.created_at,
            } for c in comments
        ]
        return Response({'comments': results}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['put'])
    def update_comment(self, request, comment_id):
        data = json.loads(request.body)
        updated = self.__commentService.update_comment(comment_id, data['content'])
        if updated:
            return Response({'message': '댓글이 갱신되었습니다.'}, status=status.HTTP_200_OK)
        return Response({'error': '댓글을 찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=True, methods=['delete'])
    def delete_comment(self, request, comment_id):
        deleted = self.__commentService.delete_comment(comment_id)
        if deleted:
            return Response({'message': '댓글이 삭제되었습니다.'}, stauts=status.HTTP_200_OK)
        return Response({'error': '댓글을 찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)
    