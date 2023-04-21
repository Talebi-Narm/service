from rest_framework.serializers import ModelSerializer

from order.models import Coupon


class CouponSerializer(ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'
