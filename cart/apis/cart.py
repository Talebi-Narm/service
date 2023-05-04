from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cart.models import PlantCart, ToolCart
from cart.serializers.cart import PlantCartSerializer, ToolCartSerializer
from common.utils.paginator import ResponsePagination


class PlantCartList(generics.CreateAPIView):
    queryset = PlantCart.objects.all()
    serializer_class = PlantCartSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = ResponsePagination

    def list(self, request):
        queryset = PlantCart.objects.filter(user=request.user, is_active=True, is_deleted=False)
        serializer = PlantCartSerializer(queryset)
        return Response(serializer.data)


class PlantCartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlantCart.objects.all()
    serializer_class = PlantCartSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = ResponsePagination
