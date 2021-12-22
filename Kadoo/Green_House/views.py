from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Coin.models import CoinManagementModel

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

class allOfMyPlant(APIView):
    def get(self, request, format=None):
        """see green house plants"""
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        _user = request.user
        myPlants = myPlant.objects.filter(user = _user, isArchived = False)
        serializer = myPlantSerializer(myPlants, many=True)
        return Response(serializer.data)

class allOfMyArchivedPlant(APIView):
    def get(self, request, format=None):
        """see green archived house plants"""
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        _user = request.user
        myPlants = myPlant.objects.filter(user = _user, isArchived = True)
        serializer = myPlantSerializer(myPlants, many=True)
        return Response(serializer.data)

class addPlantToMyGreenHouse(APIView):
    def post(self, request, format=None):
        """add to green house plants"""
        getData = addPlantSerializer(data=request.data)
        if getData.is_valid():
            if request.user.is_anonymous:
                return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
            if Plant.objects.filter(id=getData.data["plant"]).exists() == False:
                return Response("This plant does NOT Exist!", status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            _user = request.user
            _plant = Plant.objects.get(id=getData.data['plant'])
            try :
                _location = location=getData.data['location']
            except:
                _location = None
            _myPlant = myPlant.objects.create(user=_user, plant=_plant, location=getData.data['location'])
            _myPlant.save()
            if _myPlant:
                CoinData = CoinManagementModel.objects.get(user=_user)
                CoinData.coin_value -= 50
                CoinData.used_plant_count += 1
                CoinData.save()
            return Response(getData.data)
        return Response(getData.errors, status=400)

class myPlants(APIView):
    def get(self, request, pk, format=None):
        """get a plant information"""
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        _myPlant = get_object_or_404(myPlant, id=pk)
        serializer = myPlantSerializer(_myPlant, many=False)
        return Response(serializer.data)

    def post(request, pk):
        """update plant in green house"""
        _myPlant = get_object_or_404(myPlant, id=pk)
        serializer = myPlantSerializer(instance =_myPlant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            if serializer:
                if serializer.data["isArchived"] == True:
                    CoinData = CoinManagementModel.objects.get(user=request.user)
                    CoinData.coin_value += 50
                    CoinData.used_plant_count -= 1
                    CoinData.save()
        return Response(serializer.data)