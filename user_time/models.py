from django.db import models
from django.contrib.auth.models import User

class UserTime(models.Model):
    user = models.ForeignKey(User)
    timeIn = models.IntegerField()
    timeOut = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s: (%d, %d)' % (self.user.username, self.timeIn, self.timeOut)

class UserTimeChange(models.Model):
    user = models.ForeignKey(User)
    timeChange = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
