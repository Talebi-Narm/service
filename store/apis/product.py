from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from store.serializers.product import *
from common.utils.paginator import *

# ----> PLANT <----
class PlantList(generics.ListCreateAPIView):
    serializer_class = PlantSerializer
    pagination_class = ResponsePagination
    permission_classes = [IsAuthenticated]

class PlantDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlantSerializer
    pagination_class = ResponsePagination
    permission_classes = [IsAuthenticated]

# ----> TOOL <----
class ToolList(generics.ListCreateAPIView):
    serializer_class = ToolSerializer
    pagination_class = ResponsePagination
    permission_classes = [IsAuthenticated]

class ToolDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ToolSerializer
    pagination_class = ResponsePagination
    permission_classes = [IsAuthenticated]
