from django import forms
from post.models import Post
from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import CustomUser

class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email') 


class CustomUserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
