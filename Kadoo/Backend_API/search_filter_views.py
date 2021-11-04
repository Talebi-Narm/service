from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PlantSerializer, ToolSerializer, TagSerializer, ImageSerializer, AlbumSerializer
from Backend.models import Plant, Tool, Tag,Image, Album

from math import inf

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

    if (higher == inf and lower == 0)
        plants = Plant.objects.all()
    elif (higher == inf):
        plants = Plant.objects.filter(price__gte = lower)
    elif (lower == 0)
        plants = Plant.objects.filter(price__lte = lower)
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

    if (higher == inf and lower == 0)
        tools = Tool.objects.all()
    elif (higher == inf):
        tools = Tool.objects.filter(price__gte = lower)
    elif (lower == 0)
        tools = Tool.objects.filter(price__lte = lower)
    else:
        tools = Tool.objects.filter(price__gte = lower, price__lte= higher)
    serializer = ToolSerializer(tools, many=True)
    return Response(serializer.data)