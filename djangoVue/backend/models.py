from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserToken(models.Model):
    user = models.OneToOneField(User, related_name='userToken', on_delete=models.CASCADE, unique=True)
    token = models.CharField(max_length=200, blank=True)
