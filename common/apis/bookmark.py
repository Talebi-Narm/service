from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from common.models import PlantBookmark, ToolBookmark
from common.serializers.bookmark import PlantBookmarkSerializer, ToolBookmarkSerializer
from common.utils.paginator import ResponsePagination


class PlantBookmarkList(generics.ListCreateAPIView):
    swagger_tags = ('bookmark',)
    serializer_class = PlantBookmarkSerializer
    pagination_class = ResponsePagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user.id
        bookmarks = PlantBookmark.objects.filter(user=user, is_active=True, is_deleted=False)
        return bookmarks


class PlantBookmarkDestroy(generics.DestroyAPIView):
    swagger_tags = ('bookmark',)
    queryset = PlantBookmark.objects.all()
    serializer_class = PlantBookmarkSerializer
    permission_classes = [IsAuthenticated]


class ToolBookmarkList(generics.ListCreateAPIView):
    swagger_tags = ('bookmark',)
    serializer_class = ToolBookmarkSerializer
    pagination_class = ResponsePagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user.id
        bookmarks = ToolBookmark.objects.filter(user=user, is_active=True, is_deleted=False)
        return bookmarks


class ToolBookmarkDestroy(generics.DestroyAPIView):
    swagger_tags = ('bookmark',)
    queryset = ToolBookmark.objects.all()
    serializer_class = ToolBookmarkSerializer
    permission_classes = [IsAuthenticated]
