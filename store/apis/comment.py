from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from common.utils.paginator import ResponsePagination
from store.models import Plant, Tool, PlantComment, ToolComment
from store.serializers.comment import PlantCommentSerializer, ToolCommentSerializer


class PlantCommentCreate(generics.CreateAPIView):
    swagger_tags = ('comment',)
    queryset = PlantComment.objects.all()
    serializer_class = PlantCommentSerializer
    pagination_class = ResponsePagination
    permission_classes = [IsAuthenticated]


class ToolCommentCreate(generics.CreateAPIView):
    swagger_tags = ('comment',)
    queryset = ToolComment.objects.all()
    serializer_class = ToolCommentSerializer
    pagination_class = ResponsePagination
    permission_classes = [IsAuthenticated]


class PlantComments(generics.ListAPIView):
    """get a plant comments"""
    swagger_tags = ('comment',)
    pagination_class = ResponsePagination

    def get(self, request, pk):
        plant = get_object_or_404(Plant, id=pk)
        comments = PlantComment.objects.filter(plant__id=pk)
        serializer = PlantCommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_serializer_class(self):
        return PlantCommentSerializer


class ToolComments(generics.ListAPIView):
    """get a tool comments"""
    swagger_tags = ('comment',)
    pagination_class = ResponsePagination

    def get(self, request, pk):
        tool = get_object_or_404(Tool, id=pk)
        comments = ToolComment.objects.filter(plant__id=pk)
        serializer = ToolCommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_serializer_class(self):
        return ToolCommentSerializer
