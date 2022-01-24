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
        '"GET" set plant\'s have calendar to true':'/makeHaveCalendarTrue/',
        '"GET" see green house plants':'/myPlants/',
        '"POST" add to green house plants':'/myPlants/',
        '"GET" see green house plants':'/myArchivedPlants/',
        '"GET" get a plant information':'/myPlantsRUD/<str:pk>/',
        '"PUT" update plant in green house':'/myPlantsRUD/<str:pk>/',
        '"DELETE" delete plant in green house':'/myPlantsRUD/<str:pk>/',
    }
    return api_urls

class haveCalendarTrue(APIView):
    def get(self, request, pk, format=None):
        """set plant's have calendar to true"""
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        _myPlant = get_object_or_404(myPlant, id=pk)
        _myPlant.haveCalendar = True
        serializer = myPlantSerializer(_myPlant, many=False)
        return Response(serializer.data)

class allOfMyPlant(APIView):
    def get(self, request, format=None):
        """see green house plants"""
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        _user = request.user
        myPlants = myPlant.objects.filter(user = _user, isArchived = False)
        serializer = myPlantSerializer(myPlants, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        """add to green house plants"""
        
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        _user = request.user
        request.data['user'] = _user.id

        getData = myPlantSerializer(data=request.data)
        if getData.is_valid():
            getData.save()

            if getData:
                CoinData = CoinManagementModel.objects.get(user=_user)
                CoinData.coin_value -= 50
                CoinData.used_plant_count += 1
                CoinData.save()
            return Response(getData.data)
        return Response(getData.errors, status=400)

class allOfMyArchivedPlant(APIView):
    def get(self, request, format=None):
        """see green archived house plants"""
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        _user = request.user
        myPlants = myPlant.objects.filter(user = _user, isArchived = True)
        serializer = myPlantSerializer(myPlants, many=True)
        return Response(serializer.data)

class myPlantsRUD(APIView):
    def get(self, request, pk, format=None):
        """get a plant information"""
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        _myPlant = get_object_or_404(myPlant, id=pk)
        serializer = myPlantSerializer(_myPlant, many=False)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """update plant in green house"""
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        _user = request.user
        _myPlant = get_object_or_404(myPlant, id=pk)
        if "name" not in request.data:
            request.data['name'] = _myPlant.name

        request.data['user'] = _user.id

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

    def delete(self, request, pk, format=None):
        """archive plant in green house"""
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)

        _myPlant = get_object_or_404(myPlant, id=pk)
        request.data['isArchived'] = True
        request.data['user'] = request.user.id
        if "name" not in request.data:
            request.data['name'] = _myPlant.name
        serializer = myPlantSerializer(instance =_myPlant, data=request.data)
        if serializer.is_valid():
            serializer.save()
        CoinData = CoinManagementModel.objects.get(user=request.user)
        CoinData.coin_value += 50
        CoinData.used_plant_count -= 1
        CoinData.save()
        return Response(serializer.errors)