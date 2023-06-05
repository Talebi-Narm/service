from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from common.models import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)

    count = models.PositiveIntegerField(null=True, blank=True)  # null for infinite
    price = models.IntegerField(null=True, blank=True)

    main_image = models.URLField(max_length=500, null=True, blank=True)
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


class Comment(BaseModel):
    text = models.TextField()
    owner = models.ForeignKey("user.User", on_delete=models.PROTECT)
    rate = models.IntegerField(
        help_text="enter integer between 1 and 5!",
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    reply_to = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    is_buyer = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    class Meta:
        abstract = True


class PlantComment(Comment):
    plant = models.ForeignKey("store.Plant", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class ToolComment(Comment):
    tool = models.ForeignKey("store.Tool", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
