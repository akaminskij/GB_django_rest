from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    user_name = models.CharField(max_length=64, null=False, default='user')
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64, unique=True)
