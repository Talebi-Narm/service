from django.db import models

from common.models import BaseModel


class Degree(models.IntegerChoices):
    ASSOCIATE = 0, "Associate"
    BACHELOR = 1, "Bachelor"
    MASTER = 2, "Master"
    DOCTORAL = 3, "Doctoral"


class Specialist(BaseModel):
    user = models.OneToOneField("user.User", on_delete=models.CASCADE, related_name="specialist")
    birth_date = models.DateField(blank=True, null=True)
    degree = models.IntegerField(choices=Degree.choices, null=True, blank=True)
    major = models.CharField(max_length=150, blank=True)
    rate = models.IntegerField('rate', default=3)
    is_busy = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username)
