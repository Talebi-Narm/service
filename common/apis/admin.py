from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from common.serializers.tag import *
from common.utils.paginator import *

class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagAdminSerializer
    pagination_class = ResponsePagination
    permission_classes = [IsAdminUser]

class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagAdminSerializer
    pagination_class = ResponsePagination
    permission_classes = [IsAdminUser]
