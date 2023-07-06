from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated

from common.utils.paginator import ResponsePagination
from store.filters.product import PlantFilter, ToolFilter
from store.models import Plant, Tool
from store.serializers.product import PlantSerializer, ToolSerializer


# ----> PLANT <----
class PlantList(generics.ListAPIView):
    queryset = Plant.objects.filter(is_active=True, is_deleted=False)
    serializer_class = PlantSerializer
    pagination_class = ResponsePagination
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = PlantFilter
    ordering_fields = ('name', 'price', 'created_at')
    search_fields = ('name',)


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
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = ToolFilter
    ordering_fields = ('name', 'price', 'created_at')
    search_fields = ('name',)


class ToolDetail(generics.RetrieveAPIView):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer
    pagination_class = ResponsePagination
    permission_classes = [IsAuthenticated]
