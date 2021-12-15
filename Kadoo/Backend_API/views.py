from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PlantSerializer, ToolSerializer, TagSerializer, ImageSerializer, AlbumSerializer
from Backend.models import Plant, Tool, Tag,Image, Album

from .SFSP_views import SFSP_Overview
from Green_House.views import GH_Overview

@api_view(['GET'])
def ProductsAPIOverview(request):
    """See All General API"""
    api_urls = {
        'how to use':'firstly add /api/ after that use the API address you want ;) ',
        'plants List':'/plantsList/',
        'plant Detail':'/plantDetail/<str:pk>/',
        'create Plant':'/createPlant/',
        'update Plant':'/updatePlant/<str:pk>/',
        'delete Plant':'/deletePlant/<str:pk>/',

        'tools List':'/toolsList/',
        'too lDetail':'/toolDetail/<str:pk>/',
        'create Tool':'/createTool/',
        'update Tool':'/updateTool/<str:pk>/',
        'delete Tool':'/deleteTool/<str:pk>/',

        'tags List':'/tagsList/',
        'tag Detail':'/tagDetail/<str:pk>/',
        'create Tag':'/createTag/',
        'update Tag':'/updateTag/<str:pk>/',
        'delete Tag':'/deleteTag/<str:pk>/',

        'albums List':'/albumsList/',
        'album Detail':'/albumDetail/<str:pk>/',
        'create Album':'/createAlbum/',
        'update Album':'/updateAlbum/<str:pk>/',
        'delete Album':'/deleteAlbum/<str:pk>/',

        'plants Tags' : '/plantsTags/',
        'tools Tags' : '/toolsTags',

        'plants With Specific Tag':'/plantsWithTag/<str:tag>/',
        'tools With Specific Tag':'/toolsWithTag/<str:tag>/',

        'get a plant tags':'/plantTags/<str:pk>/',
        'get a tool tags':'/toolTags/<str:pk>/',

        'images List':'/imagesList/',
        'Specific plant album Images':'/plantAlbumImages/<str:pk>/',
        'Specific tool album Images':'/toolAlbumImages/<str:pk>/',
        'add image to a specific Album':'/addImageToAlbum/<str:pk>/'
    }
    api_urls.update(SFSP_Overview())
    api_urls.update(GH_Overview())
    return Response(api_urls)


# Plant
@api_view(['GET'])
def plantList(request):
    """Get All Plants"""
    plants = Plant.objects.all()
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def plantDetail(request, pk):
    """Get a Plant Detail"""
    plants = get_object_or_404(Plant, id=pk)
    serializer = PlantSerializer(plants, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createPlant(request):
    """Create a New Plant"""
    album = Album.objects.create(name=request.data['name'])
    request.data['album'] = album.id
    serializer = PlantSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def updatePlant(request, pk):
    """Update an Exisiting Plant"""
    plant = get_object_or_404(Plant, id=pk)
    serializer = PlantSerializer(instance = plant, data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deletePlant(request, pk):
    """Delete A Plant"""
    plant = get_object_or_404(Plant, id=pk)
    plant.delete()
    return Response('Item successfully deleted !')

# Tool
@api_view(['GET'])
def toolList(request):
    """See All Tools List"""
    tools = Tool.objects.all()
    serializer = ToolSerializer(tools, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def toolDetail(request, pk):
    """Get this Tool Detail"""
    tools = get_object_or_404(Tool, id=pk)
    serializer = ToolSerializer(tools, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createTool(request):
    """Create New Tool"""
    album = Album.objects.create(name=request.data['name'])
    request.data['album'] = album.id
    serializer = ToolSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def updateTool(request, pk):
    """Update an Existing Tool"""
    tool = get_object_or_404(Tool, id=pk)
    serializer = ToolSerializer(instance = tool, data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTool(request, pk):
    """Delete a Tool"""
    tool = get_object_or_404(Tool, id=pk)
    tool.delete()
    return Response('Item successfully deleted !')

# Tag
@api_view(['GET'])
def tagList(request):
    """See All Tags List"""
    tags = Tag.objects.all()
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def tagDetail(request, pk):
    """Get a Tag Details"""
    tags = get_object_or_404(Tag, id=pk)
    serializer = TagSerializer(tags, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createTag(request):
    """Create a New Tag"""
    serializer = TagSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def updateTag(request, pk):
    """Update A Tag"""
    tag = get_object_or_404(Tag, id=pk)
    serializer = TagSerializer(instance = tag, data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTag(request, pk):
    """Delete A Tag"""
    tag = get_object_or_404(Tag, id=pk)
    tag.delete()
    return Response('Item successfully deleted !')

@api_view(['GET'])
def plantsTags(request):
    """Get All Plants Tag"""
    tags = Tag.objects.all().filter(usage='Plants')
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data)
  
@api_view(['GET'])
def toolsTags(request):
    """Get All Tools Tag"""
    tags = Tag.objects.all().filter(usage='Tools')
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def plantsWithSpecificTag(request, pk):
    """Get Plants with Specific Tag"""
    tag = get_object_or_404(Tag, id=pk)
    plants = tag.plant_set.all()
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def toolsWithSpecificTag(request, pk):
    """Get Tools With Specific Tag"""
    tag = get_object_or_404(Tag, id=pk)
    tools = tag.tool_set.all()
    serializer = ToolSerializer(tools, many=True)
    return Response(serializer.data)

# Album
@api_view(['GET'])
def albumList(request):
    """Get Album List"""
    albums = Album.objects.all()
    serializer = AlbumSerializer(albums, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def albumDetail(request, pk):
    """Get an Album Detail"""
    albums = get_object_or_404(Album, id=pk)
    serializer = AlbumSerializer(albums, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createAlbum(request):
    """Create a New Album"""
    serializer = AlbumSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def updateAlbum(request, pk):
    """Update an Existing Album"""
    album = get_object_or_404(Album, id=pk)
    serializer = AlbumSerializer(instance = album, data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteAlbum(request, pk):
    """Delete an Album"""
    album = get_object_or_404(Album, id=pk)
    album.delete()
    return Response('Item successfully deleted !')

@api_view(['GET'])
def getPlantsAlbumImages(request, pk):
    """Get Plants Images"""
    plantAlbum = get_object_or_404(Plant, id=pk)
    album = get_object_or_404(Album, name=plantAlbum)
    images = album.image_set.all()
    serializer = ImageSerializer(images, many=True)

    return Response(serializer.data)

# images
@api_view(['GET'])
def getToolsAlbumImages(request, pk):
    """Get Tools Images"""
    toolAlbum = get_object_or_404(Tool, id=pk)
    album = get_object_or_404(Album, name=toolAlbum)
    images = album.image_set.all()
    serializer = ImageSerializer(images, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def imageList(request):
    """Get All Images"""
    images = Image.objects.all()
    serializer = ImageSerializer(images, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createImage(request, pk):
    """Create a New Image"""
    album = get_object_or_404(Album, id=pk)
    request.data['album'] = pk
    serializer = ImageSerializer(data = request.data)
    
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# get tags of a product
@api_view(['GET'])
def plantTags(request, pk):
    """Get Tags Of a Plant"""
    tags = get_object_or_404(Plant, id=pk).tags
    if tags.count() == 0:
        return Response('No Tags !')
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def toolTags(request, pk):
    """Get Tags Of a Tool"""
    tags = get_object_or_404(Tool, id=pk).tags
    if tags.count() == 0:
        return Response('No Tags !')
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data)
    return Response(serializer.data)
