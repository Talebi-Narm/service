from django.db import models
import uuid
from common.models import BaseModel


class CoinManagement(BaseModel):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True)
    coin_value = models.IntegerField('coin_value', default=200)
    used_plant_count = models.IntegerField(blank=True, default=0)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class LastSeenLog(BaseModel):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class LastWateringLog(BaseModel):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
