from django.urls import path
from api.views import PostListAPIView, PostDetailAPIView, PostCreateAPIView


urlpatterns = [
    path('posts/', PostListAPIView.as_view(), name='post_list_api'),
    path('posts/<int:pk>/edit/', PostDetailAPIView.as_view(), name='post_detail_api'),
    path('posts/create/', PostCreateAPIView.as_view(), name='post_create_api'),
]
