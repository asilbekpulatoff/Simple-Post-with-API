from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('post.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('account/', include('account.urls')),
]

