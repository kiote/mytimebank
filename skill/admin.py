from django.contrib import admin

from .models import Skill
from .models import UserSkill

admin.site.register(Skill)
admin.site.register(UserSkill)
