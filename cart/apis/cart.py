from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cart.models import PlantCart, ToolCart
from cart.serializers.cart import PlantCartSerializer, ToolCartSerializer
from common.utils.paginator import ResponsePagination


class PlantCartList(generics.ListCreateAPIView):
    serializer_class = PlantCartSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = ResponsePagination

    def list(self, request):
        queryset = PlantCart.objects.filter(user=request.user, is_active=True, is_deleted=False)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class PlantCartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlantCart.objects.all()
    serializer_class = PlantCartSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = ResponsePagination


class ToolCartList(generics.ListCreateAPIView):
    serializer_class = ToolCartSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = ResponsePagination

    def list(self, request):
        queryset = ToolCart.objects.filter(user=request.user, is_active=True, is_deleted=False)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ToolCartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToolCart.objects.all()
    serializer_class = ToolCartSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = ResponsePagination
