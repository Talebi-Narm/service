from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from store.serializers.product import *
from common.utils.paginator import *

class PlantList(generics.ListCreateAPIView):
    serializer_class = PlantAdminSerializer
    pagination_class = ResponsePagination
    permission_classes = [IsAdminUser]

class PlantDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlantAdminSerializer
    pagination_class = ResponsePagination
    permission_classes = [IsAdminUser]

class ToolList(generics.ListCreateAPIView):
    serializer_class = ToolAdminSerializer
    pagination_class = ResponsePagination
    permission_classes = [IsAdminUser]

class ToolDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ToolAdminSerializer
    pagination_class = ResponsePagination
    permission_classes = [IsAdminUser]
