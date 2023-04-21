from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from common.utils.paginator import *
from store.serializers.product import *


# ----> PLANT <----
class PlantList(generics.ListAPIView):
    queryset = Plant.objects.filter(is_active=True, is_deleted=False)
    serializer_class = PlantSerializer
    pagination_class = ResponsePagination
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name', 'count', 'price', 'environment', 'water', 'light', 'growth_rate', 'tags')


class PlantDetail(generics.RetrieveAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    pagination_class = ResponsePagination
    permission_classes = [IsAuthenticated]


# ----> TOOL <----
class ToolList(generics.ListAPIView):
    queryset = Tool.objects.filter(is_active=True, is_deleted=False)
    serializer_class = ToolSerializer
    pagination_class = ResponsePagination
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name', 'count', 'price', 'tags')


class ToolDetail(generics.RetrieveAPIView):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer
    pagination_class = ResponsePagination
    permission_classes = [IsAuthenticated]
