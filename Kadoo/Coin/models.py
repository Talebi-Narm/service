from django.db import models
import uuid

class CoinManagementModel(models.Model):

    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = False)
    user = models.ForeignKey('Users.Member', on_delete=models.CASCADE)
    coin_vlaue = models.IntegerField('coin_value', default=200)
    used_plant_count = models.IntegerField(blank = True, default=0)
    last_update = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return str(self.id)

class LastSeenLogModel(models.Model):

    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = False)
    user = models.ForeignKey('Users.Member', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add = True)
    
    def __str__(self):
        return str(self.id)

class LastWateringLogModel(models.Model):

    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = False)
    user = models.ForeignKey('Users.Member', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add = True)
    
    def __str__(self):
        return str(self.id)


