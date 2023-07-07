from django.urls import path

from order.apis.order import OrderList, OrderDetail
from .api import CouponListAPIView, CouponRetrieveAPIView

urlpatterns = [
    path('coupons', CouponListAPIView.as_view(), name='coupon-list'),
    path('coupons/<uuid:pk>', CouponRetrieveAPIView.as_view(), name='coupon-detail'),

    path('order/', OrderList.as_view(), name='order-list'),
    path('order/<uuid:pk>/', OrderDetail.as_view(), name='order-detail')
]
