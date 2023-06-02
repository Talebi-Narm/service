from django.db import models

from common.models import BaseModel


class UserPlant(BaseModel):
    user = models.ForeignKey('user.User', on_delete=models.PROTECT)

    nickname = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    image_url = models.URLField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    has_calendar = models.BooleanField(default=False)

    def __str__(self):
        return self.nickname
