from django.db import models
import uuid


from Users.models import NewUser
from Backend.models import Plant, Tool

class PlantCartModel(models.Model):

    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = False)
    user = models.ForeignKey('Users.NewUser', on_delete=models.CASCADE)
    plant_item = models.ForeignKey('Backend.Plant', on_delete=models.CASCADE)
    plant_count = models.IntegerField(blank = True, default=0)
    description = models.TextField(null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateField(auto_now = True)
    is_approved = models.BooleanField(default=False)
    def __str__(self):
        return str(self.id)

    #class Meta :
        #unique_together = [['user','plant_item']]
        
class ToolCartModel(models.Model):

    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = False)
    user = models.ForeignKey('Users.NewUser', on_delete=models.CASCADE)
    tool_item = models.ForeignKey('Backend.Tool', on_delete=models.CASCADE)
    tool_count = models.IntegerField(blank = True, default=0)
    is_approved = models.BooleanField(default=False)
    description = models.TextField(null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateField(auto_now = True)

    def __str__(self):
        return str(self.id)

    #class Meta :
        #unique_together = [['user','tool_item']]

class OrderModel(models.Model):

    status_quantifiers = (
       ('approved', 'approved'), 
       ('preparing', 'preparing'), 
       ('ready to deliver', 'ready to deliver'),
       ('delivering', 'delivering'), 
       ('complete', 'complete'),
    )

    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = False)
    user = models.ForeignKey('Users.NewUser', on_delete=models.CASCADE)
    order_plants = models.ManyToManyField("PlantCartModel", blank=True)
    order_tools = models.ManyToManyField("ToolCartModel", blank=True)
    status = models.CharField(max_length = 50, choices = status_quantifiers, default='approved', null = True, blank = True)
    total_price = models.IntegerField(blank = True, default=0)
    description = models.TextField(null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True)
    is_delivered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
