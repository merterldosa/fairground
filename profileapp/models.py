# pragmatic/pragmatic/models.py
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    # Profile 과 user 를 하나씩 연결해준다.
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)