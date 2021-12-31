from django.db import models
from Backend.models import Plant
from Users.models import NewUser
import uuid

class myPlant(models.Model):
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = False)
    user = models.ForeignKey('Users.NewUser', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null = True, blank = True)
    image = models.ImageField(null = True, blank = True)
    location = models.CharField(max_length=50, null=True, blank=True)
    isArchived = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add = True, blank=True)
    modified = models.DateField(auto_now = True, blank=True)

    def __str__(self):
        return  "{0} {1}".format(self. name, self.user)

    @property
    def image_url(self):
        try :
            img = self.image.url
        except :
            img = ''
        return img