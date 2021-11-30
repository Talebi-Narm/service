from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *
from Backend.models import Plant, Tool, Tag,Image, Album

# Overview
def SFSP_Overview():
    api_urls = {
        # plants filter and search
        'search in plants by name':'/plantsByName/',
        'search in plants by price':'/plantsByPrice/',
        'search in plants by environment':'/plantsByEnvironment/',
        'search in plants by water':'/plantsByWater/',
        'search in plants by light':'/plantsByLight/',
        'search in plants by growth rate':'/plantsByGrowthRate/',
        'search in plants by tags':'/plantsByTags/',

        # tools filter and search
        'search in tools by name':'/toolsByName/',
        'search in tools by price':'/toolsByPrice/',
        'search in tools by tags':'/toolsByTags/',

        # note :
        '--------note for sorting ------':'------(kind = "ASC" for ascending and "DES" for descending)----',
        # sorting
        'sorting plants':'/plantsSort/',
        'sorting tools':'/toolsSort/',

        # pagination
        'pagination plants':'/plantsPagination/',
        'pagination tools':'/toolsPagination/',

        # advance search
        'advance search in plants':'/plantsAdvanceSearch/',
        'advance search in tools':'/toolsAdvanceSearch/',
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
@api_view(['POST'])
def plantsByName(request):
    getData = nameSerializer(data=request.data)
    if getData.is_valid():

        sort = getData.data['sort']
        pagination = getData.data['pagination']

        plants = Plant.objects.filter(name__contains = getData.data['name'])

        if (sort is not None):
            plants = sorting(plants, sort['kind'], sort['order'])

        if(pagination is not None):
            plants = paginator(plants, pagination['count'], pagination['page'])
            data['pageCount'] = floor(plants.count()/pagination['count']) +1
            
        serializer = PlantSerializer(plants, many=True)

        data['data'] = serializer.data

        return Response(data)
    return Response(getData.errors)
    
@api_view(['POST'])
def plantsByPrice(request):
    getData = priceSerializer(data=request.data)
    if getData.is_valid():

        data = {'pageCount':1}

        sort = getData.data['sort']
        pagination = getData.data['pagination']

        lower = getData.data['lower']
        higher = getData.data['higher']

        if (lower is not None and higher is not None):
            if (higher == -1 and lower == 0):
                plants = Plant.objects.all()
            elif (higher == -1):
                plants = Plant.objects.filter(price__gte = lower)
            elif (lower == 0):
                plants = Plant.objects.filter(price__lte = higher)
            else:
                plants = Plant.objects.filter(price__gt = lower, price__lt= higher)

        if (sort is not None):
            plants = sorting(plants, sort['kind'], sort['order'])

        if(pagination is not None):
            plants = paginator(plants, pagination['count'], pagination['page'])
            data['pageCount'] = floor(plants.count()/pagination['count']) +1
            
        serializer = PlantSerializer(plants, many=True)

        data['data'] = serializer.data

        return Response(data)
    return Response(getData.errors) 

@api_view(['POST'])
def plantsByEnvironment(request):
    getData = environmentSerializer(data=request.data)
    if getData.is_valid():

        data = {'pageCount':1}

        sort = getData.data['sort']
        pagination = getData.data['pagination']

        plants = Plant.objects.filter(environment = getData.data['environment'])

        if (sort is not None):
            plants = sorting(plants, sort['kind'], sort['order'])

        if(pagination is not None):
            plants = paginator(plants, pagination['count'], pagination['page'])
            data['pageCount'] = floor(plants.count()/pagination['count']) +1
            
        serializer = PlantSerializer(plants, many=True)

        data['data'] = serializer.data

        return Response(data)
    return Response(getData.errors)

@api_view(['POST'])
def plantsByWater(request):
    getData = waterSerializer(data=request.data)
    if getData.is_valid():

        data = {'pageCount':1}

        sort = getData.data['sort']
        pagination = getData.data['pagination']

        plants = Plant.objects.filter(water = getData.data['water'])

        if (sort is not None):
            plants = sorting(plants, sort['kind'], sort['order'])

        if(pagination is not None):
            plants = paginator(plants, pagination['count'], pagination['page'])
            data['pageCount'] = floor(plants.count()/pagination['count']) +1
            
        serializer = PlantSerializer(plants, many=True)

        data['data'] = serializer.data

        return Response(data)
    return Response(getData.errors)

@api_view(['POST'])
def plantsByLight(request):
    getData = lightSerializer(data=request.data)
    if getData.is_valid():

        data = {'pageCount':1}

        sort = getData.data['sort']
        pagination = getData.data['pagination']

        plants = Plant.objects.filter(light = getData.data['light'])

        if (sort is not None):
            plants = sorting(plants, sort['kind'], sort['order'])

        if(pagination is not None):
            plants = paginator(plants, pagination['count'], pagination['page'])
            data['pageCount'] = floor(plants.count()/pagination['count']) +1
            
        serializer = PlantSerializer(plants, many=True)

        data['data'] = serializer.data

        return Response(data)
    return Response(getData.errors)

@api_view(['POST'])
def plantsByGrowthRate(request):
    getData = growthRateSerializer(data=request.data)
    if getData.is_valid():

        data = {'pageCount':1}

        sort = getData.data['sort']
        pagination = getData.data['pagination']

        plants = Plant.objects.filter(growthRate = getData.data['growthRate'])

        if (sort is not None):
            plants = sorting(plants, sort['kind'], sort['order'])

        if(pagination is not None):
            plants = paginator(plants, pagination['count'], pagination['page'])
            data['pageCount'] = floor(plants.count()/pagination['count']) +1
            
        serializer = PlantSerializer(plants, many=True)

        data['data'] = serializer.data

        return Response(data)
    return Response(getData.errors)

@api_view(['POST'])
def plantsByTags():
    getData = tagsSerializer(data=request.data)
    if getData.is_valid():

        data = {'pageCount':1}

        sort = getData.data['sort']
        pagination = getData.data['pagination']

        plants = Plant.objects.all()
        for tag in tags:
            tag = findTag(tag)
            if tag != None:
                plants = plants.filter(tags__in=[tag.id])

        if (sort is not None):
            plants = sorting(plants, sort['kind'], sort['order'])

        if(pagination is not None):
            plants = paginator(plants, pagination['count'], pagination['page'])
            data['pageCount'] = floor(plants.count()/pagination['count']) +1
            
        serializer = PlantSerializer(plants, many=True)

        data['data'] = serializer.data

        return Response(data)
    return Response(getData.errors)

# advance
@api_view(['POST'])
def plantsAdvanceSearch(request):
    getData = plantAdvanceSerializer(data=request.data)
    if getData.is_valid():

        data = {'pageCount':1}

        plants = Plant.objects.all()
        sort = getData.data['sort']
        pagination = getData.data['pagination']

        _name = getData.data['name']
        price = getData.data['price']
        _environment = getData.data['environment']
        _water = getData.data['water']
        _light = getData.data['light']
        _growthRate = getData.data['growthRate']
        tags = getData.data['tags']
        onlyAvailables = getData['onlyAvailables']
        
        if (onlyAvailables is not None):
            plants = plants.filter(count__gt = 0)

        if (_name is not None):
            plants = plants.filter(name__contains = _name)

        if (price is not None):
            lower = price['lower']
            higher = price['higher']
            if (lower is not None and higher is not None):
                if (higher == -1 and lower == 0):
                    pass
                elif (higher == -1):
                    plants = plants.filter(price__gte = lower)
                elif (lower == 0):
                    plants = plants.filter(price__lte = higher)
                else:
                    plants = plants.filter(price__gt = lower, price__lt= higher)

        if (_environment is not None):
            plants = plants.filter(environment = _environment)

        if (_water is not None):
            plants = plants.filter(water = _water)

        if (_light is not None):
            plants = plants.filter(light = _light)

        if (_growthRate is not None):
            plants = plants.filter(growthRate = _growthRate)

        for tag in tags:
            tag = findTag(tag)
            if tag is not None:
                plants = plants.filter(tags__in=[tag.id])

        if (sort is not None):
            if (sort['kind'] is not None and sort['order'] is not None):
                plants = sorting(plants, sort['kind'], sort['order'])

        if(pagination is not None):
            if (pagination['count'] is not None and pagination['page'] is not None):
                plants = paginator(plants, pagination['count'], pagination['page'])
                data['pageCount'] = floor(plants.count()/pagination['count']) +1
            
        serializer = PlantSerializer(plants, many=True)

        data['data'] = serializer.data

        return Response(data)
    return Response(getData.errors)

# filters for tools
@api_view(['POST'])
def toolsByName(request, _name, _paginator, _sorting):
    getData = nameSerializer(data=request.data)
    if getData.is_valid():

        data = {'pageCount':1}

        sort = getData.data['sort']
        pagination = getData.data['pagination']

        tools = Tool.objects.filter(name__contains = getData.data['name'])

        if (sort is not None):
            tools = sorting(tools, sort['kind'], sort['order'])

        if(pagination is not None):
            tools = paginator(tools, pagination['count'], pagination['page'])
            data['pageCount'] = floor(tools.count()/pagination['count']) +1
            
        serializer = ToolSerializer(tools, many=True)

        data['data'] = serializer.data

        return Response(data)
    return Response(getData.errors)

@api_view(['POST'])
def toolsByPrice(request, prices:str, _paginator, _sorting):
    getData = priceSerializer(data=request.data)
    if getData.is_valid():

        data = {'pageCount':1}

        sort = getData.data['sort']
        pagination = getData.data['pagination']

        lower = getData.data['lower']
        higher = getData.data['higher']

        if( lower is not None and higher is not None):
            if (higher == -1 and lower == 0):
                tools = Tool.objects.all()
            elif (higher == -1):
                tools = Tool.objects.filter(price__gte = lower)
            elif (lower == 0):
                tools = Tool.objects.filter(price__lte = higher)
            else:
                tools = Tool.objects.filter(price__gt = lower, price__lt= higher)

        if (sort is not None):
            tools = sorting(tools, sort['kind'], sort['order'])

        if(pagination is not None):
            tools = paginator(tools, pagination['count'], pagination['page'])
            data['pageCount'] = floor(tools.count()/pagination['count']) +1
            
        serializer = ToolSerializer(tools, many=True)

        data['data'] = serializer.data

        return Response(data)
    return Response(getData.errors)

@api_view(['POST'])
def toolsByTags(request):
    getData = tagsSerializer(data=request.data)
    if getData.is_valid():

        data = {'pageCount':1}

        sort = getData.data['sort']
        pagination = getData.data['pagination']

        tools = Tool.objects.all()
        for tag in tags:
            tag = findTag(tag)
            if tag != None:
                tools = tools.filter(tags__in=[tag.id])

        if (sort is not None):
            tools = sorting(tools, sort['kind'], sort['order'])

        if(pagination is not None):
            tools = paginator(tools, pagination['count'], pagination['page'])
            data['pageCount'] = floor(tools.count()/pagination['count']) +1
            
        serializer = ToolSerializer(tools, many=True)

        data['data'] = serializer.data

        return Response(data)
    return Response(getData.errors)
# advance
@api_view(['POST'])
def toolsAdvanceSearch(request):
    getData = plantAdvanceSerializer(data=request.data)
    if getData.is_valid():

        data = {'pageCount':1}

        tools = Tool.objects.all()

        sort = getData.data['sort']
        pagination = getData.data['pagination']

        _name = getData.data['name']
        price = getData.data['price']
        tags = getData.data['tags']
        onlyAvailables = getData['onlyAvailables']
        
        if (onlyAvailables is not None):
            tools = tools.filter(count__gt = 0)

        if (_name is not None):
            tools = tools.filter(name__contains = _name)

        if (price is not None):
            lower = price['lower']
            higher = price['higher']
            if (lower is not None and higher is not None):
                if (higher == -1 and lower == 0):
                    pass
                elif (higher == -1):
                    tools = tools.filter(price__gte = lower)
                elif (lower == 0):
                    tools = tools.filter(price__lte = higher)
                else:
                    tools = tools.filter(price__gt = lower, price__lt= higher)

        for tag in tags:
            tag = findTag(tag)
            if tag is not None:
                tools = tools.filter(tags__in=[tag.id])

        if (sort is not None):
            if (sort['kind'] is not None and sort['order'] is not None):
                tools = sorting(tools, sort['kind'], sort['order'])

        if(pagination is not None):
            if (pagination['count'] is not None and pagination['page'] is not None):
                tools = paginator(tools, pagination['count'], pagination['page'])
                data['pageCount'] = floor(tools.count()/pagination['count']) +1
            
        serializer = ToolSerializer(tools, many=True)

        data['data'] = serializer.data

        return Response(data)
    return Response(getData.errors)

# plants sorting
@api_view(['POST'])
def plantsSort(request):
    getData = sortSerializer(data=request.data)
    if getData.is_valid():
        plants = Plant.objects.all()
        kind = getData.data['kind']
        order = getData.data['order']
        if (sort['kind'] is not None and sort['order'] is not None):
            plants = sorting(plants,kind,order)
        serializer = PlantSerializer(plants, many=True)
        return Response(serializer.data)
    return Response(getData.errors)

# tools sorting
@api_view(['POST'])
def toolsSort(request):
    getData = sortSerializer(data=request.data)
    if getData.is_valid():
        tools = Tool.objects.all()
        kind = getData.data['kind']
        order = getData.data['order']
        if (kind is not None and order is not None):
            tools = sorting(tools,kind,order)
        serializer = ToolSerializer(tools, many=True)
        return Response(serializer.data)
    return Response(getData.errors)

# plants pagination
@api_view(['POST'])
def plantsPagination(request):
    getData = paginatorSerializer(data=request.data)
    if getData.is_valid():
        data = {}
        plants = Plant.objects.all()
        count = getData.data['count']
        page = getData.data['page']
        if (count is not None and page is not None):
            data['pageCount'] = floor(tools.count()/count) +1
            plants = paginator(plants, count, page)
        serializer = PlantSerializer(plants, many=True)
        data['data'] = serializer.data
        return Response(data)
    return Response(getData.errors)

# tools pagination
@api_view(['POST'])
def toolsPagination(request):
    getData = paginatorSerializer(data=request.data)
    if getData.is_valid():
        data = {}
        tools = Tool.objects.all()
        count = getData.data['count']
        page = getData.data['page']
        if (count is not None and page is not None):
            data['pageCount'] = floor(tools.count()/count) +1
            tools = paginator(tools, count, page)
        serializer = ToolSerializer(tools, many=True)
        data['data'] = serializer.data
        return Response(data)
    return Response(getData.errors)