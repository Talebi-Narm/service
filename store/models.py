from django.db import models

from common.models import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)

    count = models.PositiveIntegerField(null=True, blank=True)  # null for infinite
    price = models.IntegerField(null=True, blank=True)

    main_image = models.ImageField(null=True, blank=True)
    album = models.JSONField(null=True, blank=True)

    tags = models.ManyToManyField("common.Tag")

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Quantifier(models.IntegerChoices):
    LOW = 0, 'low'
    MEDIUM = 1, 'medium'
    MUCH = 2, 'much'


class Condition(models.IntegerChoices):
    TROPICAL = 0, 'tropical'
    COLD = 1, 'cold'
    NONE = 2, 'none'


class Plant(Product):
    environment = models.IntegerField(choices=Condition.choices, null=True, blank=True)
    water = models.IntegerField(choices=Quantifier.choices, null=True, blank=True)
    light = models.IntegerField(choices=Quantifier.choices, null=True, blank=True)
    growth_rate = models.IntegerField(choices=Quantifier.choices, null=True, blank=True)


class Tool(Product):
    pass
