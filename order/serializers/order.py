from rest_framework.serializers import ModelSerializer

from order.models import Order


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        exclude = ('created_at', 'updated_at', 'deleted_at', 'is_deleted', 'is_active')
