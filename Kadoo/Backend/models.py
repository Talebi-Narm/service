from django.db import models
import uuid

class Plant(models.Model):

    quantifiers = (
       ('low', 'low'), 
       ('medium', 'medium'), 
       ('much', 'much'), 
    )

    conditions = (
        ('tropical', 'tropical'), 
        ('cold', 'cold'), 
        ('none', 'none'), 
    )
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = False)
    name = models.CharField(max_length = 100, unique = True)
    description = models.TextField(null = True, blank = True)
    count = models.IntegerField(default = 0, blank = True)
    image = models.ImageField(null = True, blank = True)
    price = models.IntegerField(null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateField(auto_now = True)
    tags = models.ManyToManyField("Tag", blank = True)
    environment = models.CharField(max_length = 50, choices = conditions, null = True, blank = True)
    water =  models.CharField(max_length = 50, choices = quantifiers, null = True, blank = True)
    light = models.CharField( max_length = 50, choices = quantifiers, null = True, blank = True)
    growthRate = models.CharField(max_length = 50, choices = quantifiers, null = True, blank = True )

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        try :
            img = self.image.url
        except :
            img = ''
        return img
        

class Tool(models.Model):
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = False)
    name = models.CharField(max_length = 100, unique = True)
    description = models.TextField(null = True, blank = True)
    count = models.IntegerField(default = 0, blank = True)
    image = models.ImageField(null = True, blank = True)
    price = models.IntegerField(null = True, blank = True)
    tags = models.ManyToManyField("Tag", blank = True)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateField(auto_now = True)

    def __str__(self):
        return self.name
        
    @property
    def image_url(self):
        try :
            img = self.image.url
        except :
            img = ''
        return img

class Tag(models.Model):
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = False)
    name = models.CharField(max_length = 50, unique = True)
    usage = models.CharField(max_length = 50, null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateField(auto_now = True)

    def __str__(self):
        return self.name + " ( for " + self.usage + " )"