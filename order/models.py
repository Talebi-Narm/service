from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from common.models import BaseModel


class Status(models.IntegerChoices):
    PENDING = 0, "Pending"
    DELIVERY = 1, "Delivery"
    COMPLETED = 2, "Completed"


class Order(BaseModel):
    plants = models.ManyToManyField("cart.PlantCart", blank=True)
    tools = models.ManyToManyField("cart.ToolCart", blank=True)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    status = models.IntegerField(choices=Status.choices, default=0)
    coupon = models.ForeignKey("order.Coupon", null=True, blank=True, on_delete=models.SET_NULL)
    price_before = models.FloatField(blank=True, null=True)
    price_after = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.user.username + " " + str(self.created_at)


class Coupon(BaseModel):
    title = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=100, unique=True)
    discount = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    count = models.PositiveIntegerField(null=True, blank=True)  # null for infinite

    def __str__(self):
        return self.title
