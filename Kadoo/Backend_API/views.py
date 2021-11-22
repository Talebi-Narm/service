from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PlantSerializer, ToolSerializer, TagSerializer
from Backend.models import Plant, Tool, Tag

@api_view(['GET'])
def ProductsAPIOverview(request):
    api_urls = {
        'plantsList':'/plantList/',
        'plantDetail':'/plantDetail/<str:pk>/',
        'createPlant':'/createPlant/',
        'updatePlant':'/updatePlant/<str:pk>/',
        'deletePlant':'/deletePlant/<str:pk>/',

        'toolsList':'/toolList/',
        'toolDetail':'/toolDetail/<str:pk>/',
        'createTool':'/createTool/',
        'updateTool':'/updateTool/<str:pk>/',
        'deleteTool':'/deleteTool/<str:pk>/',

        'tagsList':'/tagList/',
        'tagDetail':'/tagDetail/<str:pk>/',
        'createTag':'/createTag/',
        'updateTag':'/updateTag/<str:pk>/',
        'deleteTag':'/deleteTag/<str:pk>/',

        'plantsWithTag':'/plantsWithTag/<str:tag>/',
        'toolsWithTag':'/toolsWithTag/<str:tag>/',
    }
    return Response(api_urls)


# Plant
@api_view(['GET'])
def plantList(request):
    plants = Plant.objects.all()
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def plantDetail(request, pk):
    plants = Plant.objects.get(id=pk)
    serializer = PlantSerializer(plants, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createPlant(request):
    serializer = PlantSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def updatePlant(request, pk):
    plant = Plant.objects.get(id=pk)
    serializer = PlantSerializer(instance = plant, data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deletePlant(request, pk):
    plant = Plant.objects.get(id=pk)
    plant.delete()
    return Response('Item successfully deleted !')

# Tool
@api_view(['GET'])
def toolList(request):
    tools = Tool.objects.all()
    serializer = ToolSerializer(tools, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def toolDetail(request, pk):
    tools = Tool.objects.get(id=pk)
    serializer = ToolSerializer(tools, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createTool(request):
    serializer = ToolSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def updateTool(request, pk):
    tool = Tool.objects.get(id=pk)
    serializer = ToolSerializer(instance = tool, data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTool(request, pk):
    tool = Tool.objects.get(id=pk)
    tool.delete()
    return Response('Item successfully deleted !')

# Tag
@api_view(['GET'])
def tagList(request):
    tags = Tag.objects.all()
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def tagDetail(request, pk):
    tags = Tag.objects.get(id=pk)
    serializer = TagSerializer(tags, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createTag(request):
    serializer = TagSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def updateTag(request, pk):
    tag = Tag.objects.get(id=pk)
    serializer = TagSerializer(instance = tag, data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTag(request, pk):
    tag = Tag.objects.get(id=pk)
    tag.delete()
    return Response('Item successfully deleted !')

@api_view(['GET'])
def plantsWithSpecificTag(request, tag_name):
    tag = Tag.objects.get(name=tag_name)
    plants = tag.plant_set.all()
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def toolsWithSpecificTag(request, tag_name):
    tag = Tag.objects.get(name=tag_name)
    tools = tag.tool_set.all()
    serializer = ToolSerializer(tools, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def plantTags(request, pk):
    tags = get_object_or_404(Plant, id=pk).tags
    if tags.count() == 0:
        return Response('No Tags !')
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def toolTags(request, pk):
    tags = get_object_or_404(Tool, id=pk).tags
    if tags.count() == 0:
        return Response('No Tags !')
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data)