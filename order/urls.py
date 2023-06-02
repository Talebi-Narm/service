from django.urls import path

from order.apis import CouponListAPIView, CouponRetrieveAPIView

urlpatterns = [
    path('coupons', CouponListAPIView.as_view(), name='coupon-list'),
    path('coupons/<uuid:pk>', CouponRetrieveAPIView.as_view(), name='coupon-detail')
]
