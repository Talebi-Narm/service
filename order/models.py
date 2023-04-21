from django.db import models

from common.models import BaseModel


# class Order(BaseModel):
#     pass


class Coupon(BaseModel):
    title = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=100, unique=True)
    discount = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    count = models.PositiveIntegerField(null=True, blank=True)  # null for infinite
