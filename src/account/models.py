from django.db import models
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q



class MultiLoginBackend(ModelBackend):

    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()

        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)

        users = UserModel._default_manager.filter(
            Q(**{UserModel.USERNAME_FIELD: username}) | Q(email__iexact=username))

        for user in users:
            if user.check_password(password):
                return user

        if not users:
            UserModel().set_password(password)
