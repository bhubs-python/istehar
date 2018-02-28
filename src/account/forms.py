from django import forms
from django.contrib.auth import authenticate
import re
from django.contrib.auth.models import User

from .models import DualModelBackend


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    email = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate', 'id': 'email'}))
    password1 = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(attrs={'class': 'validate'}))
    password2 = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(attrs={'class': 'validate'}))





# login form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'validate', 'id': 'icon_prefix',}))
    password = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(attrs={'class': 'validate', 'id': 'password'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if len(username) < 1:
            raise forms.ValidationError("Enter Username!")
        else:
            if len(password) < 8:
                raise forms.ValidationError("Password is too short!")
            else:
                user = DualModelBackend.authenticate(self, username=username, password=password)
                if not user or not user.is_active:
                    raise forms.ValidationError("Username or Password not matched!")
        return self.cleaned_data


    def login(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user = DualModelBackend.authenticate(self, username=username, password=password)
        return user
