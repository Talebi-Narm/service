from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response


from .serializers import PlantSerializer, ToolSerializer, TagSerializer, ImageSerializer, AlbumSerializer
from Backend.models import Plant, Tool, Tag,Image, Album

from math import inf

# Overview
def searchAndFilterOverview():
    api_urls = {
        # plants filter and search
        'search in plants by name':'/plantsByName/<str:name>/',
        'search in plants by price':'/plantsByPrice/<str:lower_price>-<str:higher_price>/',
        'search in plants by environment':'/plantsByEnvironment/<str:environment>/',
        'search in plants by water':'/plantsByWater/<str:water>/',
        'search in plants by light':'/plantsByLight/<str:light>/',
        'search in plants by growth rate':'/plantsByGrowthRate/<str:growthRate>/',
        'search in plants by tags':'/plantsByTags/<str:tag1>-<str:tag2>-.../',

        # tools filter and search
        'search in tools by name':'/toolsByName/<str:name>/',
        'search in tools by price':'/toolsByPrice/<str:lower_price>-<str:higher_price>/',
        'search in tools by tags':'/toolsByTags/<str:tag1>-<str:tag2>-.../',

        # advance search
        'advance search in plants':'/plantsAdvanceSearch/<str:name>-<str:lower_price>-<str:higher_price>-<str:environment>-<str:water>-<str:light>-<str:growthRate>-<str:tag1>-<str:tag2>-.../',
        'advance search in tools':'/toolsAdvanceSearch/<str:name>-<str:tag1>-<str:tag2>-.../',
        }
    return api_urls

# universal defs
def findTag(_name):
    try:
        tag = Tag.objects.get(name=_name)
    except:
        tag = None
    return tag

# filters for plants
@api_view(['GET'])
def plantsByName(request, _name):
    plants = Plant.objects.filter(name__contains = _name)
    serializer = PlantSerializer(plants, many=True)
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
def plantsByEnvironment(request, _environment):
    plants = Plant.objects.filter(environment = _environment)
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def plantsByWater(request, _water):
    plants = Plant.objects.filter(water = _water)
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def plantsByLight(request, _light):
    plants = Plant.objects.filter(light = _light)
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def plantsByGrowthRate(request, _growthRate):
    plants = Plant.objects.filter(growthRate = _growthRate)
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def plantsByTags(request, tags:str):
    tags:list = tags.split('-')
    plants = Plant.objects.all()

    for tag in tags:
        tag = findTag(tag)
        if tag != None:
            plants = plants.filter(tags__in=[tag.id])

    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)

# advance
@api_view(['GET'])
def plantsAdvanceSearch(request, filters:str):
    filters = filters.split('-')
    try:
        tags = filters[7:]
    except:
        tags = []
    
    plants = Plant.objects.all()

    try:
        _name = filters[0]
    except:
        _name = ''

    try:
        lower = int(filters[1])
    except:
        lower = 0

    try:
        higher = int(filters[2])
    except:
        higher = inf

    try:
        _environment = filters[3]
    except:
        _environment = ''

    try:
        _water = filters[4]
    except:
        _water = ''
    
    try:
        _light = filters[5]
    except:
        _light = ''

    try:
        _growthRate = filters[6]
    except:
        _growthRate = ''
    
    if (_name != ''):
        plants = plants.filter(name__contains = _name)

    if (higher == inf and lower == 0):
        pass
    elif (higher == inf):
        plants = plants.filter(price__gte = lower)
    elif (lower == 0):
        plants = plants.filter(price__lte = higher)
    else:
        plants = plants.filter(price__gt = lower, price__lt= higher)

    if (_environment != ''):
        plants = plants.filter(environment = _environment)

    if (_water != ''):
        plants = plants.filter(water = _water)

    if (_light != ''):
        plants = plants.filter(light = _light)

    if (_growthRate != ''):
        plants = plants.filter(growthRate = _growthRate)

    for tag in tags:
        tag = findTag(tag)
        if tag != None:
            plants = plants.filter(tags__in=[tag.id])

    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)


# filters for tools
@api_view(['GET'])
def toolsByName(request, _name):
    tools = Tool.objects.filter(name__contains = _name)
    serializer = ToolSerializer(tools, many=True)
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
def toolsByTags(request, tags:str):
    tags:list = tags.split('-')
    tools = Tool.objects.all()

    for tag in tags:
        tag = findTag(tag)
        if tag != None:
            tools = tools.filter(tags__in=[tag.id])

    serializer = ToolSerializer(tools, many=True)
    return Response(serializer.data)

# advance
@api_view(['GET'])
def toolsAdvanceSearch(request, filters:str):
    filters = filters.split('-')
    try:
        tags = filters[3:]
    except:
        tags = []
    
    tools = Tool.objects.all()

    try:
        _name = filters[0]
    except:
        _name = ''

    try:
        lower = int(filters[1])
    except:
        lower = 0

    try:
        higher = int(filters[2])
    except:
        higher = inf

    if (_name != ''):
        plants = plants.filter(name__contains = _name)

    if (higher == inf and lower == 0):
        pass
    elif (higher == inf):
        tools = tools.filter(price__gte = lower)
    elif (lower == 0):
        tools = tools.filter(price__lte = higher)
    else:
        tools = tools.filter(price__gt = lower, price__lt= higher)

    for tag in tags:
        tag = findTag(tag)
        if tag != None:
            tools = tools.filter(tags__in=[tag.id])

    serializer = ToolSerializer(tools, many=True)
    return Response(serializer.data)


# plants sorting
@api_view(['GET'])
def plantsSortByName(request, kind):
    plants = Plant.objects.all()

    if kind == 'ACS':
        plants = plants.order_by('name')
    elif kind == 'DES':
        plants = plants.order_by('name').reverse()
    
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def plantsSortByPrice(request, kind):
    plants = Plant.objects.all()

    if kind == 'ACS':
        plants = plants.order_by('price')
    elif kind == 'DES':
        plants = plants.order_by('price').reverse()
    
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def plantsSortByCreateDate(request):
    plants = Plant.objects.all().order_by('created').reverse()
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)

# tools sorting
@api_view(['GET'])
def toolsSortByName(request, kind):
    tools = Tool.objects.all()

    if kind == 'ACS':
        tools = tools.order_by('name')
    elif kind == 'DES':
        tools = tools.order_by('name').reverse()
    
    serializer = ToolSerializer(tools, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def toolsSortByPrice(request, kind):
    tools = Tool.objects.all()

    if kind == 'ACS':
        tools = tools.order_by('price')
    elif kind == 'DES':
        tools = tools.order_by('price').reverse()
    
    serializer = ToolSerializer(tools, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def toolsSortByCreateDate(request):
    tools = Tool.objects.all().order_by('created').reverse()
    serializer = ToolSerializer(tools, many=True)
    return Response(serializer.data)