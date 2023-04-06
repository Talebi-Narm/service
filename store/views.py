from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *
from common.models import Tag
from .models import Plant, Tool

# plant
class plants(APIView):
    """
    List of Plant objects or create one
    """
    def get(self, request, format=None):
        """Get All Plants"""
        plants = Plant.objects.all()
        serializer = PlantSerializer(plants, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """Create a New Plant"""
        serializer = PlantSerializerCU(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class plantsRUD(APIView):
    """
    Retrieve, update or delete a plant instance.
    """
    def get_object(self, pk):
        return get_object_or_404(Plant, id=pk)

    def get(self, request, pk, format=None):
        """Get a Plant Detail"""
        plant = self.get_object(pk)
        serializer = PlantSerializer(plant, many=False)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """Update an Existing Plant"""
        plant = self.get_object(pk)
        serializer = PlantSerializerCU(instance = plant, data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        """Delete A Plant"""
        plant = self.get_object(pk)
        plant.delete()
        plant.save()
        return Response('Item successfully deleted !')

# Tool
class tools(APIView):
    """
    List of Tool objects or create one
    """
    def get(self, request, format=None):
        """Get All Tools"""
        tools = Tool.objects.all()
        serializer = ToolSerializer(tools, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """Create a New Tool"""
        serializer = ToolSerializerCU(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class toolsRUD(APIView):
    """
    Retrieve, update or delete a tool instance.
    """
    def get_object(self, pk):
        return get_object_or_404(Tool, id=pk)

    def get(self, request, pk, format=None):
        """Get a Tool Detail"""
        tool = self.get_object(pk)
        serializer = ToolSerializer(tool, many=False)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """Update an Existing Tool"""
        tool = self.get_object(pk)
        serializer = ToolSerializerCU(instance = tool, data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        """Delete A Tool"""
        tool = self.get_object(pk)
        tool.delete()
        return Response('Item successfully deleted !')

# Tag
class tags(APIView):
    """
    List of Tag objects or create one
    """
    def get(self, request, format=None):
        """Get All Tags"""
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """Create a New Tag"""
        serializer = TagSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class tagsRUD(APIView):
    """
    Retrieve, update or delete a tag instance.
    """
    def get_object(self, pk):
        return get_object_or_404(Tag, id=pk)

    def get(self, request, pk, format=None):
        """Get a Tag Detail"""
        tag = self.get_object(pk)
        serializer = TagSerializer(tag, many=False)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """Update an Existing Tag"""
        tag = self.get_object(pk)
        serializer = TagSerializer(instance = tag, data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        """Delete A Tag"""
        tag = self.get_object(pk)
        tag.delete()
        return Response('Item successfully deleted !')

class plantsTags(APIView):
    def get(self, request, format=None):
        """Get All Plants Tag"""
        tags = Tag.objects.all().filter(usage='Plants')
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

class toolsTags(APIView):
    def get(self, request, format=None):
        """Get All Tools Tag"""
        tags = Tag.objects.all().filter(usage='Tools')
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

class plantsWithSpecificTag(APIView):
    def get(self, request, pk, format=None):
        """Get Plants with Specific Tag"""
        tag = get_object_or_404(Tag, id=pk)
        plants = tag.plant_set.all()
        serializer = PlantSerializer(plants, many=True)
        return Response(serializer.data)

class toolsWithSpecificTag(APIView):
    def get(self, request, pk, format=None):
        """Get Tools With Specific Tag"""
        tag = get_object_or_404(Tag, id=pk)
        tools = tag.tool_set.all()
        serializer = ToolSerializer(tools, many=True)
        return Response(serializer.data)

# get tags of a product
class plantTags(APIView):
    def get(self, request, pk, format=None):
        """Get Tags Of a Plant"""
        tags = get_object_or_404(Plant, id=pk).tags
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

class toolTags(APIView):
    def get(self, request, pk, format=None):
        """Get Tags Of a Tool"""
        tags = get_object_or_404(Tool, id=pk).tags
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
