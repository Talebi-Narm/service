from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from store.serializers.product import *
from common.utils.paginator import *

# ----> PLANT <----
class PlantList(generics.ListAPIView):
    serializer_class = PlantSerializer
    pagination_class = ResponsePagination
    permission_classes = [IsAuthenticated]

class PlantDetail(generics.RetrieveAPIView):
    serializer_class = PlantSerializer
    pagination_class = ResponsePagination
    permission_classes = [IsAuthenticated]

# ----> TOOL <----
class ToolList(generics.ListAPIView):
    serializer_class = ToolSerializer
    pagination_class = ResponsePagination
    permission_classes = [IsAuthenticated]

class ToolDetail(generics.RetrieveAPIView):
    serializer_class = ToolSerializer
    pagination_class = ResponsePagination
    permission_classes = [IsAuthenticated]
