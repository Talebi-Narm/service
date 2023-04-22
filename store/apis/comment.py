from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from common.utils.paginator import ResponsePagination
from store.models import Plant, Tool, PlantComment, ToolComment
from store.serializers.comment import PlantCommentSerializer, ToolCommentSerializer


class PlantCommentCreate(generics.CreateAPIView):
    queryset = PlantComment.objects.all()
    serializer_class = PlantCommentSerializer
    pagination_class = ResponsePagination
    permission_classes = [IsAuthenticated]


class ToolCommentCreate(generics.CreateAPIView):
    queryset = PlantComment.objects.all()
    serializer_class = ToolCommentSerializer
    pagination_class = ResponsePagination
    permission_classes = [IsAuthenticated]


class PlantComments(GenericAPIView):
    def get(self, request, pk):
        plant = get_object_or_404(Plant, id=pk)
        comments = PlantComment.objects.filter(plant__id=plant.id)
        serializer = PlantCommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ToolComments(GenericAPIView):
    def get(self, request, pk):
        plant = get_object_or_404(Tool, id=pk)
        comments = PlantComment.objects.filter(plant__id=plant.id)
        serializer = ToolCommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
