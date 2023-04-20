from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from store.serializers.product import *
from common.utils.paginator import *

from django_filters.rest_framework import DjangoFilterBackend

class PlantList(generics.ListCreateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantAdminSerializer
    pagination_class = ResponsePagination
    permission_classes = [IsAdminUser]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name', 'count', 'price', 'environment', 'water', 'light', 'growth_rate', 'tags')

class PlantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantAdminSerializer
    pagination_class = ResponsePagination
    permission_classes = [IsAdminUser]

class ToolList(generics.ListCreateAPIView):
    queryset = Tool.objects.all()
    serializer_class = ToolAdminSerializer
    pagination_class = ResponsePagination
    permission_classes = [IsAdminUser]

class ToolDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tool.objects.all()
    serializer_class = ToolAdminSerializer
    pagination_class = ResponsePagination
    permission_classes = [IsAdminUser]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name', 'count', 'price', 'tags')