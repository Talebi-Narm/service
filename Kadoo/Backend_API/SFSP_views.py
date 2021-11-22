from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PlantSerializer, ToolSerializer, TagSerializer, ImageSerializer, AlbumSerializer
from Backend.models import Plant, Tool, Tag,Image, Album

from math import inf

# Overview
def SFSP_Overview():
    api_urls = {
        # plants filter and search
        'search in plants by name':'/plantsByName/<name>/<count>-<page>/<order_by>-<kind>/',
        'search in plants by price':'/plantsByPrice/<lower_price>-<higher_price>/<count>-<page>/<order_by>-<kind>/',
        'search in plants by environment':'/plantsByEnvironment/<environment>/<count>-<page>/<order_by>-<kind>/',
        'search in plants by water':'/plantsByWater/<water>/<count>-<page>/<order_by>-<kind>/',
        'search in plants by light':'/plantsByLight/<light>/<count>-<page>/<order_by>-<kind>/',
        'search in plants by growth rate':'/plantsByGrowthRate/<growthRate>/<count>-<page>/<order_by>-<kind>/',
        'search in plants by tags':'/plantsByTags/<tag1>-<tag2>-.../<count>-<page>/<order_by>-<kind>/',

        # tools filter and search
        'search in tools by name':'/toolsByName/<name>/<count>-<page>/<order_by>-<kind>/',
        'search in tools by price':'/toolsByPrice/<lower_price>-<higher_price>/<count>-<page>/<order_by>-<kind>/',
        'search in tools by tags':'/toolsByTags/<tag1>-<tag2>-.../<count>-<page>/<order_by>-<kind>/',

        # note :
        '--------note for sorting ------':'------(kind = "ASC" for ascending and "DES" for descending)----',
        # plants sorting
        'sorting plants by name':'/plantsSortByName/<kind>/',
        'sorting plants by price':'/plantsSortByPrice/<kind>/',
        'sorting plants by crated time (newest)':'/plantsSortByNewest/',

        # tools sorting
        'sorting tools by name':'/toolsSortByName/<kind>/',
        'sorting tools by price':'/toolsSortByPrice/<kind>/',
        'sorting tools by crated time (newest)':'/toolsSortByNewest/',

        # advance search
        'advance search in plants':'/plantsAdvanceSearch/<name>-<lower_price>-<higher_price>-<environment>-<water>-<light>-<growthRate>-<tag1>-<tag2>-.../<count>-<page>/<order_by>-<kind>/',
        'advance search in tools':'/toolsAdvanceSearch/<name>-<lower_price>-<higher_price>-<tag1>-<tag2>-.../<count>-<page>/<order_by>-<kind>/',
        }
    return api_urls

# universal defs
def findTag(_name):
    try:
        tag = Tag.objects.get(name=_name)
    except:
        tag = None
    return tag

def paginator(myList: list, count, page):
    first = (page-1)*count
    try:
        end = (page)*count
    except:
        end = len(myList)

    return myList[first:end]

def sorting(myList: list, by , order):
    if (by == 'name' or by == 'price' or by == 'time'):
        if (by == 'time'):
            return myList.order_by('created').reverse()
        if (order == 'ASC'):
            myList = myList.order_by(by)
        elif (order == 'DES'):
            myList = myList.order_by(by).reverse()
    
    return myList

# filters for plants
@api_view(['GET'])
def plantsByName(request, _name , _paginator, _sorting):
    _paginator = _paginator.split('-')
    _sorting = _sorting.split('-')

    try:
        by = sorting[0]
        order = sorting[1]
    except:
        _sorting = None

    try:
        count = int(_paginator[0])
        page = int(_paginator[1])
    except:
        _paginator = None

    plants = Plant.objects.filter(name__contains = _name)

    if(_paginator != None):
        plants = paginator(plants, count, page)

    if (_sorting != None):
        plants = sorting(plants, by, order)
        
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def plantsByPrice(request, prices, _paginator, _sorting):
    prices = prices.split('-')
    _paginator = _paginator.split('-')
    _sorting = _sorting.split('-')

    try:
        by = sorting[0]
        order = sorting[1]
    except:
        _sorting = None

    lower = 0
    higher = inf

    try:
        count = int(_paginator[0])
        page = int(_paginator[1])
    except:
        _paginator = None
        
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

    if(_paginator != None):
        plants = paginator(plants, count, page)
    
    if (_sorting != None):
        plants = sorting(plants, by, order)
        
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def plantsByEnvironment(request, _environment, _paginator, _sorting):
    _paginator = _paginator.split('-')
    _sorting = _sorting.split('-')

    try:
        by = sorting[0]
        order = sorting[1]
    except:
        _sorting = None
        
    try:
        count = int(_paginator[0])
        page = int(_paginator[1])
    except:
        _paginator = None

    plants = Plant.objects.filter(environment = _environment)

    if(_paginator != None):
        plants = paginator(plants, count, page)
    
    if (_sorting != None):
        plants = sorting(plants, by, order)
        
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def plantsByWater(request, _water, _paginator, _sorting):
    _paginator = _paginator.split('-')
    _sorting = _sorting.split('-')

    try:
        by = sorting[0]
        order = sorting[1]
    except:
        _sorting = None
        
    try:
        count = int(_paginator[0])
        page = int(_paginator[1])
    except:
        _paginator = None

    plants = Plant.objects.filter(water = _water)

    if(_paginator != None):
        plants = paginator(plants, count, page)
    
    if (_sorting != None):
        plants = sorting(plants, by, order)
        
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def plantsByLight(request, _light, _paginator, _sorting):
    _paginator = _paginator.split('-')
    _sorting = _sorting.split('-')

    try:
        by = sorting[0]
        order = sorting[1]
    except:
        _sorting = None
        
    try:
        count = int(_paginator[0])
        page = int(_paginator[1])
    except:
        _paginator = None

    plants = Plant.objects.filter(light = _light)

    if(_paginator != None):
        plants = paginator(plants, count, page)
    
    if (_sorting != None):
        plants = sorting(plants, by, order)
        
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def plantsByGrowthRate(request, _growthRate, _paginator, _sorting):
    _paginator = _paginator.split('-')
    _sorting = _sorting.split('-')

    try:
        by = sorting[0]
        order = sorting[1]
    except:
        _sorting = None
        
    try:
        count = int(_paginator[0])
        page = int(_paginator[1])
    except:
        _paginator = None

    plants = Plant.objects.filter(growthRate = _growthRate)

    if(_paginator != None):
        plants = paginator(plants, count, page)
    
    if (_sorting != None):
        plants = sorting(plants, by, order)
        
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def plantsByTags(request, tags:str, _paginator, _sorting):
    tags:list = tags.split('-')
    _paginator = _paginator.split('-')
    _sorting = _sorting.split('-')

    try:
        by = sorting[0]
        order = sorting[1]
    except:
        _sorting = None
        

    try:
        count = int(_paginator[0])
        page = int(_paginator[1])
    except:
        _paginator = None

    plants = Plant.objects.all()

    for tag in tags:
        tag = findTag(tag)
        if tag != None:
            plants = plants.filter(tags__in=[tag.id])

    if(_paginator != None):
        plants = paginator(plants, count, page)
    
    if (_sorting != None):
        plants = sorting(plants, by, order)
        
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)

# advance
@api_view(['GET'])
def plantsAdvanceSearch(request, filters:str, _paginator, _sorting):
    filters = filters.split('-')
    _paginator = _paginator.split('-')
    _sorting = _sorting.split('-')

    try:
        by = sorting[0]
        order = sorting[1]
    except:
        _sorting = None
        

    try:
        count = int(_paginator[0])
        page = int(_paginator[1])
    except:
        _paginator = None

    try:
        tags = filters[7:]
    except:
        tags = []
     
    plants = Plant.objects.all()

    try:
        _name = filters[0]
    except:
        _name = None

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
        _environment = None

    try:
        _water = filters[4]
    except:
        _water = None
    
    try:
        _light = filters[5]
    except:
        _light = None

    try:
        _growthRate = filters[6]
    except:
        _growthRate = None
    
    if (_name != None):
        plants = plants.filter(name__contains = _name)

    if (higher == inf and lower == 0):
        pass
    elif (higher == inf):
        plants = plants.filter(price__gte = lower)
    elif (lower == 0):
        plants = plants.filter(price__lte = higher)
    else:
        plants = plants.filter(price__gt = lower, price__lt= higher)

    if (_environment != None):
        plants = plants.filter(environment = _environment)

    if (_water != None):
        plants = plants.filter(water = _water)

    if (_light != None):
        plants = plants.filter(light = _light)

    if (_growthRate != None):
        plants = plants.filter(growthRate = _growthRate)

    for tag in tags:
        tag = findTag(tag)
        if tag != None:
            plants = plants.filter(tags__in=[tag.id])

    if(_paginator != None):
        plants = paginator(plants, count, page)
    
    if (_sorting != None):
        plants = sorting(plants, by, order)
        
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)


# filters for tools
@api_view(['GET'])
def toolsByName(request, _name, _paginator, _sorting):
    _paginator = _paginator.split('-')
    _sorting = _sorting.split('-')

    try:
        by = sorting[0]
        order = sorting[1]
    except:
        _sorting = None
        
    try:
        count = int(_paginator[0])
        page = int(_paginator[1])
    except:
        _paginator = None

    tools = Tool.objects.filter(name__contains = _name)

    if(_paginator != None):
        tools = paginator(tools, count, page)
    
    if (_sorting != None):
        tools = sorting(tools, by, order)
        
    serializer = ToolSerializer(tools, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def toolsByPrice(request, prices:str, _paginator, _sorting):
    prices = prices.split('-')
    _paginator = _paginator.split('-')
    _sorting = _sorting.split('-')

    try:
        by = sorting[0]
        order = sorting[1]
    except:
        _sorting = None

    try:
        count = int(_paginator[0])
        page = int(_paginator[1])
    except:
        _paginator = None

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
    
    if(_paginator != None):
        tools = paginator(tools, count, page)
    
    if (_sorting != None):
        tools = sorting(tools, by, order)
    
    serializer = ToolSerializer(tools, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def toolsByTags(request, tags:str, _paginator, _sorting):
    tags:list = tags.split('-')
    _paginator = _paginator.split('-')
    _sorting = _sorting.split('-')

    try:
        by = sorting[0]
        order = sorting[1]
    except:
        _sorting = None

    try:
        count = int(_paginator[0])
        page = int(_paginator[1])
    except:
        _paginator = None

    tools = Tool.objects.all()

    for tag in tags:
        tag = findTag(tag)
        if tag != None:
            tools = tools.filter(tags__in=[tag.id])
    
    if(_paginator != None):
        tools = paginator(tools, count, page)
    
    if (_sorting != None):
        tools = sorting(tools, by, order)
    
    serializer = ToolSerializer(tools, many=True)
    return Response(serializer.data)

# advance
@api_view(['GET'])
def toolsAdvanceSearch(request, filters:str, _paginator, _sorting):
    filters = filters.split('-')
    _paginator = _paginator.split('-')
    _sorting = _sorting.split('-')

    try:
        by = sorting[0]
        order = sorting[1]
    except:
        _sorting = None
        
    try:
        count = int(_paginator[0])
        page = int(_paginator[1])
    except:
        _paginator = None

    try:
        tags = filters[3:]
    except:
        tags = []
    
    tools = Tool.objects.all()

    try:
        _name = filters[0]
    except:
        _name = None

    try:
        lower = int(filters[1])
    except:
        lower = 0

    try:
        higher = int(filters[2])
    except:
        higher = inf

    if (_name != None):
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
    
    if(_paginator != None):
        tools = paginator(tools, count, page)
    
    if (_sorting != None):
        tools = sorting(tools, by, order)
    
    serializer = ToolSerializer(tools, many=True)
    return Response(serializer.data)

# plants sorting
@api_view(['GET'])
def plantsSortByName(request, kind):
    plants = Plant.objects.all()
    plants = sorting(plants, 'name' , kind)
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def plantsSortByPrice(request, kind):
    plants = Plant.objects.all()
    plants = sorting(plants, 'price' , kind)
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def plantsSortByCreateDate(request):
    plants = Plant.objects.all()
    plants = sorting(plants, 'time' , 'DES')
    serializer = PlantSerializer(plants, many=True)
    return Response(serializer.data)

# tools sorting
@api_view(['GET'])
def toolsSortByName(request, kind):
    tools = Tool.objects.all()
    tools = sorting(tools, 'name' , kind)
    serializer = ToolSerializer(tools, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def toolsSortByPrice(request, kind):
    tools = Tool.objects.all()
    tools = sorting(tools, 'price' , kind)
    serializer = ToolSerializer(tools, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def toolsSortByCreateDate(request):
    tools = Tool.objects.all()
    tools = sorting(tools, 'time' , 'DES')
    serializer = ToolSerializer(tools, many=True)
    return Response(serializer.data)