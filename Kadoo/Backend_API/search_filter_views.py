from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PlantSerializer, ToolSerializer, TagSerializer, ImageSerializer, AlbumSerializer
from Backend.models import Plant, Tool, Tag,Image, Album

from math import inf

def searchAndFilterOverview():
    api_urls = {
        'search in plants by name':'/plantsByName/<str:_name>/',
        'search in tools by name':'/toolsByName/<str:_name>/',
        'search in plants by price':'/plantsByPrice/<str:lower>-<str:higher>/',
        'search in tools by price':'/toolsByPrice/<str:lower>-<str:higher>/',
        'advance search in plants':'/plantsAdvanceSearch/<str:lower>-<str:higher>-<str:environment>-<str:water>-<str:light>-<str:growthRate>/',
    }
    return api_urls

@api_view(['GET'])
def plantsByName(request, _name):
    plants = Plant.objects.filter(name__contains = _name)
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def toolsByName(request, _name):
    tools = Tool.objects.filter(name__contains = _name)
    serializer = ToolSerializer(tools, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def plantsByPrice(request, prices:str):
    prices = prices.split('-')
    lower = 0
    higher = inf

    try:
        lower = int(prices[0])
    except:
        lower = 0

    try:
        higher = int(prices[1])
    except:
        higher = inf

    if (higher == inf and lower == 0):
        plants = Plant.objects.all()
    elif (higher == inf):
        plants = Plant.objects.filter(price__gte = lower)
    elif (lower == 0):
        plants = Plant.objects.filter(price__lte = higher)
    else:
        plants = Plant.objects.filter(price__gt = lower, price__lt= higher)
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def toolsByPrice(request, prices:str):
    prices = prices.split('-')
    lower = 0
    higher = inf

    try:
        lower = int(prices[0])
    except:
        lower = 0

    try:
        higher = int(prices[1])
    except:
        higher = inf

    if (higher == inf and lower == 0):
        tools = Tool.objects.all()
    elif (higher == inf):
        tools = Tool.objects.filter(price__gte = lower)
    elif (lower == 0):
        tools = Tool.objects.filter(price__lte = higher)
    else:
        tools = Tool.objects.filter(price__gte = lower, price__lte= higher)
    serializer = ToolSerializer(tools, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def plantsAdvanceSearch(request, filters:str):
    filters = filters.split('-')
    plants = Plant.objects.all()

    try:
        lower = int(filters[0])
    except:
        lower = 0

    try:
        higher = int(filters[1])
    except:
        higher = inf

    try:
        _environment = filters[2]
    except:
        _environment = ''

    try:
        _water = filters[3]
    except:
        _water = ''
    
    try:
        _light = filters[4]
    except:
        _light = ''

    try:
        _growthRate = filters[5]
    except:
        _growthRate = ''
    
    if (higher == inf and lower == 0):
        plants = Plant.objects.all()
    elif (higher == inf):
        plants = Plant.objects.filter(price__gte = lower)
    elif (lower == 0):
        plants = Plant.objects.filter(price__lte = higher)
    else:
        plants = Plant.objects.filter(price__gt = lower, price__lt= higher)

    if (_environment != ''):
        plants = plants.filter(environment = _environment)

    if (_water != ''):
        plants = plants.filter(water = _water)

    if (_light != ''):
        plants = plants.filter(light = _light)

    if (_growthRate != ''):
        plants = plants.filter(growthRate = _growthRate)

    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)