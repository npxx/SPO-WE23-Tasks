from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

import bcrypt

class MyCustomBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None
