from django.db import models

from common.models import BaseModel


def upload_to(instance, filename):
    filename = str(instance.pk) + '.' + filename.split('.')[-1]
    return 'images/{filename}'.format(filename=filename)


class UserPlant(BaseModel):
    user = models.ForeignKey('user.User', on_delete=models.PROTECT)

    nickname = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=True, blank=True)

    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    has_calendar = models.BooleanField(default=False)

    def __str__(self):
        return self.nickname
