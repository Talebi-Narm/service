from django.forms import model_to_dict
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from order.models import Order


class OrderSerializer(ModelSerializer):
    price_before = SerializerMethodField("get_before")
    price_after = SerializerMethodField("get_after")

    plants_detail = SerializerMethodField("get_plants")
    tools_detail = SerializerMethodField("get_tools")

    def get_before(self, obj):
        temp = 0
        for cart in obj.plants.all():
            temp += cart.plant.price
        for cart in obj.tools.all():
            temp += cart.tool.price
        return temp

    def get_after(self, obj):
        if obj.coupon is not None:
            return self.get_before(obj) * obj.coupon.discount / 100
        return self.get_before(obj)

    def get_plants(self, obj):
        temp = []
        for cart in obj.plants.all():
            plant = model_to_dict(cart.plant)
            plant['cart_count'] = cart.count
            temp.append(plant)
        return temp

    def get_tools(self, obj):
        temp = []
        for cart in obj.tools.all():
            tool = model_to_dict(cart.tool)
            tool['cart_count'] = cart.count
            temp.append(tool)
        return temp

    class Meta:
        model = Order
        exclude = ('created_at', 'updated_at', 'deleted_at', 'is_deleted', 'is_active')
        read_only_fields = ["price_before", "price_after"]
