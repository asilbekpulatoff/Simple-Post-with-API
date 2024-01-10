from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from post.models import Post
from api.serializers import PostSerializer


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.filter(public=True)
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.filter(public=True)
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


