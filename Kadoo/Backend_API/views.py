from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
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
        album = Album.objects.create(name=request.data['name'])
        request.data['album'] = album.id
        request.data['kind'] = "Plant"
        serializer = PlantSerializer(data = request.data)
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
        serializer = PlantSerializer(instance = plant, data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk, format=None):
        """Delete A Plant"""
        plant = self.get_object(pk)
        plant.delete()
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
        album = Album.objects.create(name=request.data['name'])
        request.data['album'] = album.id
        request.data['kind'] = "Tool"
        serializer = ToolSerializer(data = request.data)
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
        serializer = ToolSerializer(instance = tool, data = request.data)
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

# Album
class albums(APIView):
    """
    List of Album objects or create one
    """
    def get(self, request, format=None):
        """Get All Albums"""
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        """Create a New Album"""
        album = Album.objects.create(name=request.data['name'])
        request.data['album'] = album.id
        request.data['kind'] = "Album"
        serializer = AlbumSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()  
        return Response(serializer.data)

class albumsRUD(APIView):
    """
    Retrieve, update or delete a album instance.
    """
    def get_object(self, pk):
        return get_object_or_404(Album, id=pk)
    
    def get(self, request, pk, format=None):
        """Get a Album Detail"""
        album = self.get_object(pk)
        serializer = AlbumSerializer(album, many=False)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """Update an Existing Album"""
        album = self.get_object(pk)
        serializer = AlbumSerializer(instance = album, data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk, format=None):
        """Delete A Album"""
        album = self.get_object(pk)
        album.delete()
        return Response('Item successfully deleted !')

# images
class getPlantsAlbumImages(APIView):
    def get(self, request, pk, format=None):
        """Get Plants Images"""
        plantAlbum = get_object_or_404(Plant, id=pk)
        album = get_object_or_404(Album, name=plantAlbum)
        images = album.image_set.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)

class getToolsAlbumImages(APIView):
    def get(self, request, pk, format=None):
        """Get Tools Images"""
        toolAlbum = get_object_or_404(Tool, id=pk)
        album = get_object_or_404(Album, name=toolAlbum)
        images = album.image_set.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)

class images(APIView):
    def get(self, request, format=None):
        """Get All Images"""
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)

class addImageToAlbum(APIView):
    def post(self, request, pk, format=None):
        """Create a New Image"""
        album = get_object_or_404(Album, id=pk)
        request.data['album'] = pk
        serializer = ImageSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

# get tags of a product
class plantTags(APIView):
    def get(self, request, pk, format=None):
        """Get Tags Of a Plant"""
        tags = get_object_or_404(Plant, id=pk).tags
        if tags.count() == 0:
            return Response('No Tags !')
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

class toolTags(APIView):
    def get(self, request, pk, format=None):
        """Get Tags Of a Tool"""
        tags = get_object_or_404(Tool, id=pk).tags
        if tags.count() == 0:
            return Response('No Tags !')
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)