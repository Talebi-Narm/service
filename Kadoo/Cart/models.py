from django.db import models
import uuid


from Users.models import NewUser
from Backend.models import Plant, Tool

class PlantCartModel(models.Model):

    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = False)
    user = models.OneToOneField(NewUser, on_delete=models.CASCADE)
    plant_item = models.OneToOneField(Plant, on_delete=models.CASCADE)
    plant_count = models.IntegerField(blank = True, default=0)
    description = models.TextField(null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateField(auto_now = True)

    def __str__(self):
        return str(self.id)
        
class ToolCartModel(models.Model):

    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = False)
    user = models.OneToOneField(NewUser, on_delete=models.CASCADE)
    tool_item = models.OneToOneField(Tool, on_delete=models.CASCADE)
    tool_count = models.IntegerField(blank = True, default=0)
    description = models.TextField(null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateField(auto_now = True)

    def __str__(self):
        return str(self.id)
