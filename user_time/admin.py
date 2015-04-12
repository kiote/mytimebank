from django.contrib import admin
from .models import UserTime
from .models import UserTimeChange

admin.site.register(UserTime)
admin.site.register(UserTimeChange)
