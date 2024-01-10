from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions, generics, status

from account.serializers import UserSerializer, CustomTokenObtainPairSerializer
from account.models import CustomUser


class SignUpView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token_data = RefreshToken.for_user(user)
        token_dict = {
            'access_token': str(token_data.access_token),
            'refresh_token': str(token_data),
        }
        headers = self.get_success_headers(serializer.data)
        return Response(token_dict, status=status.HTTP_201_CREATED, headers=headers)
    
    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = (permissions.AllowAny,)


class LogoutView(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh_token')
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'Chiqildi!'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Noto\'g\'ri token!'}, status=status.HTTP_400_BAD_REQUEST)






from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from post.forms import CustomUserCreationForm, CustomUserLoginForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/sign_up.html', {'form': form})


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  # data argumentini qo'shing
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})


def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('home')
