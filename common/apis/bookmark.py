from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from common.models import PlantBookmark, ToolBookmark
from common.serializers.bookmark import PlantBookmarkSerializer, ToolBookmarkSerializer
from common.utils.paginator import ResponsePagination


class PlantBookmarkList(generics.ListCreateAPIView):
    swagger_tags = ('bookmark',)
    serializer_class = PlantBookmarkSerializer
    pagination_class = ResponsePagination
    permission_classes = [IsAuthenticated]

    def list(self, request):
        user = request.user.id
        bookmarks = PlantBookmark.objects.filter(user=user, is_active=True, is_deleted=False)
        serializer = self.get_serializer(bookmarks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


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

    def list(self, request):
        user = request.user.id
        bookmarks = ToolBookmark.objects.filter(user=user, is_active=True, is_deleted=False)
        serializer = self.get_serializer(bookmarks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ToolBookmarkDestroy(generics.DestroyAPIView):
    swagger_tags = ('bookmark',)
    queryset = ToolBookmark.objects.all()
    serializer_class = PlantBookmarkSerializer
    permission_classes = [IsAuthenticated]
