from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField, DateTimeField, EmailField


class CustomUser(AbstractUser):
    name= CharField(max_length=50, default='Anonymous')
    email =EmailField(max_length=254, unique=True, blank=False)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    phone=CharField(max_length=20, blank=True, null=True)
    gender = CharField(max_length=10, blank=True, null=True)
    session_token=CharField(max_length=10, default=0)
    created_at= DateTimeField(auto_now_add=True)
    modified_at = DateTimeField(auto_now=True)