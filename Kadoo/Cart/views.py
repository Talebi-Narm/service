from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import response, status
from rest_framework.views import APIView
from Backend.models import Plant
from Cart.models import PlantCartModel

from Cart.serializers import CartPlantSerializer

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'add-plant-to-cart':'/AddPlantToCart/',
    }
    return Response(api_urls)


class AddPlantToCart(APIView):
 def post(self, request, format='json'):
  serializer = CartPlantSerializer(data=request.data)
  if serializer.is_valid():
   #Get All Data
   userToAdd = request.user
   PlantToAdd = Plant.objects.get(id=serializer.data["id"])
   PlantToAddCount = serializer.data["count"]
   PlantToAddDescription = serializer.data["description"]
   #Make Cart Plant Item
   PlantCartItem = PlantCartModel.objects.create(user=userToAdd, plant_item=PlantToAdd, plant_count=PlantToAddCount, description=PlantToAddDescription)
   #Save Plant Item
   PlantCartItem.save()
   if PlantCartItem:
    json = serializer.data
    return response(json, status=status.HTTP_201_CREATED)
   return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RemovePlantFromCart(APIView):
 def post(self, request, format='json'):
  serializer = CartPlantSerializer(data=request.data)
  if serializer.is_valid():
   #Get All Data
   userToAdd = request.user
   PlantToAdd = Plant.objects.get(name=serializer.data["id"])
   PlantToAddCount = serializer.data["count"]
   PlantToAddDescription = serializer.data["description"]
   #Make Cart Plant Item
   PlantCartItem = PlantCartModel(user=userToAdd, plant_item=PlantToAdd, plant_count=PlantToAddCount, description=PlantToAddDescription)
   #Save Plant Item
   PlantCartItem.save()
   if PlantCartItem:
    json = serializer.data
    return response(json, status=status.HTTP_201_CREATED)
   return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
