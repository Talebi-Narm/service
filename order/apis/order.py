from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from common.utils.paginator import ResponsePagination
from order.models import Order
from order.serializers.order import OrderSerializer


class OrderList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    pagination_class = ResponsePagination

    def get_queryset(self):
        queryset = Order.objects.filter(user=self.request.user, is_active=True, is_deleted=False)
        return queryset


class OrderDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    pagination_class = ResponsePagination

    def get_queryset(self):
        queryset = Order.objects.filter(user=self.request.user, is_active=True, is_deleted=False)
        return queryset
