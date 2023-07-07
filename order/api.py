from rest_framework.generics import ListAPIView, RetrieveAPIView
from order.models import Coupon
from order.serializers.coupon import CouponSerializer


class CouponListAPIView(ListAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer


class CouponRetrieveAPIView(RetrieveAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
