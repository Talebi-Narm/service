from django.db import models

from common.models import BaseModel


class UserPlant(BaseModel):
    user = models.ForeignKey('user.User', on_delete=models.PROTECT)

    nickname = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    image = models.ImageField(null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)

    is_archived = models.BooleanField(default=False)
    has_calendar = models.BooleanField(default=False)

    def __str__(self):
        return self.nickname
