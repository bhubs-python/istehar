from django import forms
from django.contrib.auth import authenticate
import re
from django.contrib.auth.models import User

from .models import MultiLoginBackend


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate'}))
    email = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'validate', 'id': 'email'}))
    password1 = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(attrs={'class': 'validate'}))
    password2 = forms.CharField(max_length=20, required=False, widget=forms.PasswordInput(attrs={'class': 'validate'}))


    def clean(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if len(username) < 1:
            raise forms.ValidationError("Enter username!")
        else:
            user_exist = User.objects.filter(username__iexact=username).exists()
            if user_exist:
                raise forms.ValidationError("Username already taken!")
            else:
                if len(email) < 1:
                    raise forms.ValidationError("Enter email address!")
                else:
                    email_correction = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
                    if email_correction == None:
                        raise forms.ValidationError("Email not correct!")
                    else:
                        email_exist = User.objects.filter(email__iexact=email).exists()
                        if email_exist:
                            raise forms.ValidationError("Email already exist!")
                        else:
                            if len(password1) < 8:
                                raise forms.ValidationError("Password is too short!")
                            else:
                                if password1 != password2:
                                    raise forms.ValidationError("Password not matched!")


    def registration(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password1 = self.cleaned_data.get('password1')

        user = User.objects.create_user(username=username, email=email)
        user.set_password(password1)

        user.save()



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
                user = MultiLoginBackend.authenticate(self, username=username, password=password)
                if not user or not user.is_active:
                    raise forms.ValidationError("Username or Password not matched!")
        return self.cleaned_data


    def login(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user = MultiLoginBackend.authenticate(self, username=username, password=password)
        return user
