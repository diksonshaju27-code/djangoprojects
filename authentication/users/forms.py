from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django import forms
from django.forms import CharField, PasswordInput
from twisted.python.formmethod import Password
from twisted.web.twcgi import CGIScript

class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1','password2','email', 'first_name', 'last_name']


class LoginForm(forms.Form):
    username=CharField()
    password=CharField(widget=forms.PasswordInput)