# posts/views.py
from rest_framework import viewsets, permissions,generics
from .models import Post, Comment,Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework import filters
from rest_framework.response import Response
from notifications.models import Notification
from rest_framework import status
from django.shortcuts import get_object_or_404

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserFeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self,request,*args, **kwargs):
        following_users = request.user.following.all()  # Get the users that the current user follows

        posts=Post.objects.filter(author__in=following_users).order_by('-created_at')      
        post_data = [
            {
                'id': post.id,
                'author': post.author.username,
                'title': post.title,
                'content': post.content,
                'created_at': post.created_at,
                'updated_at': post.updated_at,
            }
            for post in posts
        ]
        return Response(post_data)
    
class LikePost(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)  # Use get_object_or_404
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        
        if created:
            # Create a notification
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                target=post
            )
            return Response({"detail": "Post liked."}, status=status.HTTP_201_CREATED)
        return Response({"detail": "Post already liked."}, status=status.HTTP_400_BAD_REQUEST)

class UnlikePost(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post =generics.get_object_or_404(Post, pk=pk)  # Use get_object_or_404
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({"detail": "Post unliked."}, status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            return Response({"detail": "Like does not exist."}, status=status.HTTP_400_BAD_REQUEST)