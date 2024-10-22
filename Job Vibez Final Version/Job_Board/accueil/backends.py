from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import People  

class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = People.objects.get(email=username)
            if user and check_password(password, user.password):
                return user
        except People.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return People.objects.get(pk=user_id)
        except People.DoesNotExist:
            return None
