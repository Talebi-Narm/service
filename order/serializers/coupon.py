from rest_framework.serializers import ModelSerializer

from order.models import Coupon


class CouponSerializer(ModelSerializer):
    class Meta:
        model = Coupon
        exclude = ('created_at', 'updated_at', 'deleted_at', 'is_deleted', 'is_active')
