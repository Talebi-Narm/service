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

        # plants sorting
        'sorting plants by name (kind = "ASC" for ascending and "DES" for descending)':'/plantsSortByName/<str:kind>/',
        'sorting plants by price (kind = "ASC" for ascending and "DES" for descending)':'/plantsSortByPrice/<str:kind>/',
        'sort by crated time (newest)':'/plantsSortByNewest/',

        # tools sorting
        'sorting tools by name (kind = "ASC" for ascending and "DES" for descending)':'/toolsSortByName/<str:kind>/',
        'sorting tools by price (kind = "ASC" for ascending and "DES" for descending)':'/toolsSortByPrice/<str:kind>/',
        'sort by crated time (newest)':'/toolsSortByNewest/',

        # advance search
        'advance search in plants':'/plantsAdvanceSearch/<str:sort>-<str:kind>-<str:name>-<str:lower_price>-<str:higher_price>-<str:environment>-<str:water>-<str:light>-<str:growthRate>-<str:tag1>-<str:tag2>-.../',
        'advance search in tools':'/toolsAdvanceSearch/<str:sort>-<str:kind>-<str:name>-<str:lower_price>-<str:higher_price>-<str:tag1>-<str:tag2>-.../',
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
    if (by != 'name' or by != 'price' or by != 'time'):
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
    plants = sorting(plants, 'time' , kind)
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
    tools = sorting(plants, 'time' , kind)
    serializer = ToolSerializer(tools, many=True)
    return Response(serializer.data)