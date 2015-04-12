from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    owner = models.ForeignKey(User)
    sex = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
