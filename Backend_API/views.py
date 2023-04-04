# from django.shortcuts import get_object_or_404
#
# from rest_framework.views import APIView
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
#
# from .serializers import PlantSerializer, PlantSerializerCU, ToolSerializer, TagSerializer, ImageSerializer, AlbumSerializer, ToolSerializerCU
# from Backend.models import Plant, Tool, Tag,Image, Album
#
# from .SFSP_views import SFSP_Overview
# from Green_House.views import GH_Overview
# from Reminder.views import Reminder_Overview
#
# class ProductsAPIOverview(APIView):
#     def get(self, request, format=None):
#         """See All General API"""
#         api_urls = {
#             'how to use':'firstly add /api/ after that use the API address you want ;) ',
#
#             '"GET" plants List':'/plants/',
#             '"GET" plant Detail':'/plantsRUD/<str:pk>/',
#             '"POST" create plant':'/plants/',
#             '"PUT" update plant':'/plantsRUD/<str:pk>/',
#             '"DELETE" delete plant':'/plantsRUD/<str:pk>/',
#
#             '"GET" tools List':'/tools/',
#             '"GET" tool Detail':'/toolsRUD/<str:pk>/',
#             '"POST" create tool':'/tools/',
#             '"PUT" update tool':'/toolsRUD/<str:pk>/',
#             '"DELETE" delete tool':'/toolsRUD/<str:pk>/',
#
#             '"GET" tags List':'/tags/',
#             '"GET" tag Detail':'/tagsRUD/<str:pk>/',
#             '"POST" create tag':'/tags/',
#             '"PUT" update tag':'/tagsRUD/<str:pk>/',
#             '"DELETE" delete tag':'/tagsRUD/<str:pk>/',
#
#             '"GET" albums List':'/albums/',
#             '"GET" album Detail':'/albumsRUD/<str:pk>/',
#             '"POST" create album':'/albums/',
#             '"PUT" update album':'/albumsRUD/<str:pk>/',
#             '"DELETE" delete album':'/albumsRUD/<str:pk>/',
#
#             '"GET" plants Tags' : '/plantsTags/',
#             '"GET" tools Tags' : '/toolsTags',
#
#             '"GET" plants With Specific Tag':'/plantsWithTag/<str:tag_name>/',
#             '"GET" tools With Specific Tag':'/toolsWithTag/<str:tag_name>/',
#
#             '"GET" get a plant tags':'/plantTags/<str:pk>/',
#             '"GET" get a tool tags':'/toolTags/<str:pk>/',
#
#             '"GET" images List':'/imageList/',
#             '"GET" Specific plant album Images':'/plantAlbumImages/<str:pk>/',
#             '"GET" Specific tool album Images':'/toolAlbumImages/<str:pk>/',
#             '"GET" add image to a specific Album':'/addImageToAlbum/<str:pk>/'
#         }
#         api_urls.update(SFSP_Overview())
#         api_urls.update(GH_Overview())
#         api_urls.update(Reminder_Overview())
#         return Response(api_urls)
#
# # plant
# class plants(APIView):
#     """
#     List of Plant objects or create one
#     """
#     def get(self, request, format=None):
#         """Get All Plants"""
#         plants = Plant.objects.all()
#         serializer = PlantSerializer(plants, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         """Create a New Plant"""
#         album = Album.objects.create(name=request.data['name'])
#         request.data['album'] = album.id
#         request.data['kind'] = "Plant"
#         serializer = PlantSerializerCU(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
#
# class plantsRUD(APIView):
#     """
#     Retrieve, update or delete a plant instance.
#     """
#     def get_object(self, pk):
#         return get_object_or_404(Plant, id=pk)
#
#     def get(self, request, pk, format=None):
#         """Get a Plant Detail"""
#         plant = self.get_object(pk)
#         serializer = PlantSerializer(plant, many=False)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         """Update an Existing Plant"""
#         plant = self.get_object(pk)
#         serializer = PlantSerializerCU(instance = plant, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
#
#     def delete(self, request, pk, format=None):
#         """Delete A Plant"""
#         plant = self.get_object(pk)
#         plant.delete()
#         plant.save()
#         return Response('Item successfully deleted !')
#
# # Tool
# class tools(APIView):
#     """
#     List of Tool objects or create one
#     """
#     def get(self, request, format=None):
#         """Get All Tools"""
#         tools = Tool.objects.all()
#         serializer = ToolSerializer(tools, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         """Create a New Tool"""
#         album = Album.objects.create(name=request.data['name'])
#         request.data['album'] = album.id
#         request.data['kind'] = "Tool"
#         serializer = ToolSerializerCU(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
#
# class toolsRUD(APIView):
#     """
#     Retrieve, update or delete a tool instance.
#     """
#     def get_object(self, pk):
#         return get_object_or_404(Tool, id=pk)
#
#     def get(self, request, pk, format=None):
#         """Get a Tool Detail"""
#         tool = self.get_object(pk)
#         serializer = ToolSerializer(tool, many=False)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         """Update an Existing Tool"""
#         tool = self.get_object(pk)
#         serializer = ToolSerializerCU(instance = tool, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
#
#     def delete(self, request, pk, format=None):
#         """Delete A Tool"""
#         tool = self.get_object(pk)
#         tool.delete()
#         return Response('Item successfully deleted !')
#
# # Tag
# class tags(APIView):
#     """
#     List of Tag objects or create one
#     """
#     def get(self, request, format=None):
#         """Get All Tags"""
#         tags = Tag.objects.all()
#         serializer = TagSerializer(tags, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         """Create a New Tag"""
#         serializer = TagSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
#
# class tagsRUD(APIView):
#     """
#     Retrieve, update or delete a tag instance.
#     """
#     def get_object(self, pk):
#         return get_object_or_404(Tag, id=pk)
#
#     def get(self, request, pk, format=None):
#         """Get a Tag Detail"""
#         tag = self.get_object(pk)
#         serializer = TagSerializer(tag, many=False)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         """Update an Existing Tag"""
#         tag = self.get_object(pk)
#         serializer = TagSerializer(instance = tag, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
#
#     def delete(self, request, pk, format=None):
#         """Delete A Tag"""
#         tag = self.get_object(pk)
#         tag.delete()
#         return Response('Item successfully deleted !')
#
# class plantsTags(APIView):
#     def get(self, request, format=None):
#         """Get All Plants Tag"""
#         tags = Tag.objects.all().filter(usage='Plants')
#         serializer = TagSerializer(tags, many=True)
#         return Response(serializer.data)
#
# class toolsTags(APIView):
#     def get(self, request, format=None):
#         """Get All Tools Tag"""
#         tags = Tag.objects.all().filter(usage='Tools')
#         serializer = TagSerializer(tags, many=True)
#         return Response(serializer.data)
#
# class plantsWithSpecificTag(APIView):
#     def get(self, request, pk, format=None):
#         """Get Plants with Specific Tag"""
#         tag = get_object_or_404(Tag, id=pk)
#         plants = tag.plant_set.all()
#         serializer = PlantSerializer(plants, many=True)
#         return Response(serializer.data)
#
# class toolsWithSpecificTag(APIView):
#     def get(self, request, pk, format=None):
#         """Get Tools With Specific Tag"""
#         tag = get_object_or_404(Tag, id=pk)
#         tools = tag.tool_set.all()
#         serializer = ToolSerializer(tools, many=True)
#         return Response(serializer.data)
#
# # Album
# class albums(APIView):
#     """
#     List of Album objects or create one
#     """
#     def get(self, request, format=None):
#         """Get All Albums"""
#         albums = Album.objects.all()
#         serializer = AlbumSerializer(albums, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         """Create a New Album"""
#         album = Album.objects.create(name=request.data['name'])
#         request.data['album'] = album.id
#         request.data['kind'] = "Album"
#         serializer = AlbumSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
#
# class albumsRUD(APIView):
#     """
#     Retrieve, update or delete a album instance.
#     """
#     def get_object(self, pk):
#         return get_object_or_404(Album, id=pk)
#
#     def get(self, request, pk, format=None):
#         """Get a Album Detail"""
#         album = self.get_object(pk)
#         serializer = AlbumSerializer(album, many=False)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         """Update an Existing Album"""
#         album = self.get_object(pk)
#         serializer = AlbumSerializer(instance = album, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
#
#     def delete(self, request, pk, format=None):
#         """Delete A Album"""
#         album = self.get_object(pk)
#         album.delete()
#         return Response('Item successfully deleted !')
#
# # images
# class getPlantsAlbumImages(APIView):
#     def get(self, request, pk, format=None):
#         """Get Plants Images"""
#         plantAlbum = get_object_or_404(Plant, id=pk)
#         album = get_object_or_404(Album, name=plantAlbum)
#         images = album.image_set.all()
#         serializer = ImageSerializer(images, many=True)
#         return Response(serializer.data)
#
# class getToolsAlbumImages(APIView):
#     def get(self, request, pk, format=None):
#         """Get Tools Images"""
#         toolAlbum = get_object_or_404(Tool, id=pk)
#         album = get_object_or_404(Album, name=toolAlbum)
#         images = album.image_set.all()
#         serializer = ImageSerializer(images, many=True)
#         return Response(serializer.data)
#
# class images(APIView):
#     def get(self, request, format=None):
#         """Get All Images"""
#         images = Image.objects.all()
#         serializer = ImageSerializer(images, many=True)
#         return Response(serializer.data)
#
# class addImageToAlbum(APIView):
#     def post(self, request, pk, format=None):
#         """Create a New Image"""
#         album = get_object_or_404(Album, id=pk)
#         request.data['album'] = pk
#         serializer = ImageSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return Response(serializer.data)
#
# # get tags of a product
# class plantTags(APIView):
#     def get(self, request, pk, format=None):
#         """Get Tags Of a Plant"""
#         tags = get_object_or_404(Plant, id=pk).tags
#         serializer = TagSerializer(tags, many=True)
#         return Response(serializer.data)
#
# class toolTags(APIView):
#     def get(self, request, pk, format=None):
#         """Get Tags Of a Tool"""
#         tags = get_object_or_404(Tool, id=pk).tags
#         serializer = TagSerializer(tags, many=True)
#         return Response(serializer.data)