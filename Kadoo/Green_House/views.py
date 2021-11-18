from django.shortcuts import get_object_or_404

from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import myPlant
from Backend.models import Plant
from .serializers import *

import uuid

def GH_Overview():
    api_urls = {
        'see green house plants':'/myPlants/',
        'see green house plants':'/myArchivedPlants/',
        'add to green house plants':'/addToMyPlants/',
        'get a plant information':'/getMyPlant/<str:pk>/',
        'update plant in green house':'/updateInMyPlants/<str:pk>/',
    }
    return api_urls

@api_view(['GET'])
def allOfMyPlant(request):
    if request.user.is_anonymous:
        return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
    _user = request.user
    myPlants = myPlant.objects.filter(user = _user, isArchived = False)
    serializer = myPlantSerializer(myPlants, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def allOfMyArchivedPlant(request):
    if request.user.is_anonymous:
        return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
    _user = request.user
    myPlants = myPlant.objects.filter(user = _user, isArchived = True)
    serializer = myPlantSerializer(myPlants, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addPlantToMyGreenHouse(request):
    serializer = addPlantSerializer(data=request.data)
    if serializer.is_valid():
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        if Plant.objects.filter(id=serializer.data["plant"]).exists() == False:
            return response.Response("This plant does NOT Exist!", status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        _user = request.user
        _plant = Plant.objects.get(id=serializer.data['plant'])
        try :
            _location = location=serializer.data['location']
        except:
            _location = None
        _myPlant = myPlant.objects.create(user=_user, plant=_plant, location=serializer.data['location'])
        _myPlant.save()
    return Response(serializer.data)

@api_view(['GET'])
def getPlant(request, pk):
    if request.user.is_anonymous:
        return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
    _myPlant = get_object_or_404(myPlant, id=pk)
    serializer = myPlantSerializer(_myPlant, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def updatePlantInMyGreenHouse(request, pk):
    _myPlant = get_object_or_404(myPlant, id=pk)
    serializer = myPlantSerializer(instance =_myPlant, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)