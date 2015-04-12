from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    description = models.CharField(max_length=400)
    endorsed_by = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserSkills(models.Model):
    user = models.ForeignKey(User)
    skill = models.ForeignKey(Skill)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
