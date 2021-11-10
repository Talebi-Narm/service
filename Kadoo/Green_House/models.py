from django.db import models
from Backend.models import Plant
from Users.models import NewUser
import uuid

class myPlant(models.Model):
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = False)
    user = models.ForeignKey('Users.NewUser', on_delete=models.CASCADE)
    plant = models.ForeignKey('Backend.Plant', on_delete=models.CASCADE)
    image = models.ImageField(null = True, blank = True)
    location = models.CharField(max_length=50, null=True, blank=True)
    isArchived = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add = True, blank=True)
    modified = models.DateField(auto_now = True, blank=True)

    def __str__(self):
        return  "{0} {1}".format(self.plant.name, self.user)
