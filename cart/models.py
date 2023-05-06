from django.db import models

from common.models import BaseModel


class Cart(BaseModel):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    count = models.IntegerField()

    class Meta:
        abstract = True


class PlantCart(Cart):
    plant = models.ForeignKey('store.Plant', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        unique_together = ('user', 'plant')


class ToolCart(Cart):
    tool = models.ForeignKey('store.Tool', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        unique_together = ('user', 'tool')

# class Order(BaseModel):
#     status_quantifiers = (
#         ('approved', 'approved'),
#         ('preparing', 'preparing'),
#         ('ready to deliver', 'ready to deliver'),
#         ('delivering', 'delivering'),
#         ('complete', 'complete'),
#     )
#
#     user = models.ForeignKey('user.User', on_delete=models.CASCADE)
#
#     order_plants = models.ManyToManyField("PlantCartModel", blank=True)
#     order_tools = models.ManyToManyField("ToolCartModel", blank=True)
#     status = models.CharField(max_length=50, choices=status_quantifiers, default='approved', null=True, blank=True)
#     total_price = models.IntegerField(blank=True, default=0)
#     description = models.TextField(null=True, blank=True)
#     created = models.DateTimeField(auto_now_add=True)
#     is_delivered = models.BooleanField(default=False)
#
#     def __str__(self):
#         return str(self.id)
#
#
# class OrderItem(BaseModel):
#     pass
