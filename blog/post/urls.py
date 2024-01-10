from django.urls import path
from .views import post_detail, post_delete, post_edit, PostListView, home, PostCreateView


urlpatterns = [
    path('', home, name='home'),
    path('post/list', PostListView.as_view(), name='post_list'),
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/detail/', post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', post_delete, name='post_delete'),
]
