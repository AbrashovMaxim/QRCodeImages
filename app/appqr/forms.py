from django import forms
from django.contrib.auth.models import User

from .models import *

class QrCreateForm(forms.Form):
    image = forms.ImageField(label='Изображение')

    class Meta:
        model = QrImageGenerator
        fields = ('image', )

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=255, label='Никнейм')
    password = forms.CharField(max_length=255, label='Пароль')
    email = forms.EmailField(label='Почта')
    first_name = forms.CharField(max_length=255, label='Имя')
    last_name = forms.CharField(max_length=255, label='Фамилия')
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, label='Никнейм')
    password = forms.CharField(max_length=255, label='Пароль')
    class Meta:
        model = User
        fields = ('username', 'password')