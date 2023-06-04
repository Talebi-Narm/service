import uuid

from django.db import models

from common.models import BaseModel


class Degree(models.IntegerChoices):
    ASSOCIATE = 0, "Associate"
    BACHELOR = 1, "Bachelor"
    MASTER = 2, "Master"
    DOCTORAL = 3, "Doctoral"


class Specialist(BaseModel):
    user = models.OneToOneField("user.User", on_delete=models.PROTECT, related_name="specialist")
    birth_date = models.DateField(blank=True, null=True)
    degree = models.IntegerField(choices=Degree.choices, null=True, blank=True)
    major = models.CharField(max_length=150, blank=True)
    rate = models.IntegerField('rate', default=3)

    def __str__(self):
        return str(self.user.username)


class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey("user.User", on_delete=models.PROTECT, related_name="tickets")
    specialist = models.ForeignKey("Specialist", on_delete=models.PROTECT, related_name="tickets", null=True)
    title = models.CharField(max_length=255)
    is_closed = models.BooleanField(default=False)
