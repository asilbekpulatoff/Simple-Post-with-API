from django.urls import path    
from account.views import signup_view, login_view, logout_view
from .views import SignUpView, CustomTokenObtainPairView, LogoutView, CustomTokenObtainPairView


urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),


    path('signup/', SignUpView.as_view(), name='signup_api'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login_api'),
    path('logout/', LogoutView.as_view(), name='logout_api'),

]


