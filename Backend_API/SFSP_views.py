# from django.shortcuts import get_object_or_404
#
# from rest_framework.views import APIView
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
#
# from .serializers import *
# from Backend.models import Plant, Tool, Tag,Image, Album
#
# from math import ceil
# import random
#
# # Overview
# def SFSP_Overview():
#     api_urls = {
#         # plants filter and search
#         '"POST" search in plants by name':'/plantsByName/',
#         '"POST" search in plants by price':'/plantsByPrice/',
#         '"POST" search in plants by environment':'/plantsByEnvironment/',
#         '"POST" search in plants by water':'/plantsByWater/',
#         '"POST" search in plants by light':'/plantsByLight/',
#         '"POST" search in plants by growth rate':'/plantsByGrowthRate/',
#         '"POST" search in plants by tags':'/plantsByTags/',
#
#         # tools filter and search
#         '"POST" search in tools by name':'/toolsByName/',
#         '"POST" search in tools by price':'/toolsByPrice/',
#         '"POST" search in tools by tags':'/toolsByTags/',
#
#         # note :
#         '--------note for sorting ------':'------(kind = "ASC" for ascending and "DES" for descending)----',
#         # sorting
#         '"POST" sorting plants':'/plantsSort/',
#         '"POST" sorting tools':'/toolsSort/',
#
#         # pagination
#         '"POST" pagination plants':'/plantsPagination/',
#         '"POST" pagination tools':'/toolsPagination/',
#         '"POST" pagination all':'/allPagination/',
#
#         # advance search
#         '"POST" advance search in plants':'/plantsAdvanceSearch/',
#         '"POST" advance search in tools':'/toolsAdvanceSearch/',
#         '"POST" advance search in all products':'/allAdvanceSearch/',
#         }
#     return api_urls
#
# # universal defs
# def findTag(_name):
#     try:
#         tag = Tag.objects.get(name=_name)
#     except:
#         tag = None
#     return tag
#
# def paginator(myList: list, count, page):
#     first = (page-1)*count
#     try:
#         end = (page)*count
#     except:
#         end = len(myList)
#
#     return myList[first:end]
#
# def sorting(myList: list, by , order):
#     if (by == 'name' or by == 'price' or by == 'time'):
#         if (by == 'time'):
#             return sorted(myList, key=lambda x:x['created'], reverse=True)
#         if (order == 'ASC'):
#             return sorted(myList, key=lambda x:x[by])
#         elif (order == 'DES'):
#             return sorted(myList, key=lambda x:x[by], reverse=True)
#
#     return myList
#
# # filters for plants
# class plantsByName(APIView):
#     def post(self, request, format=None):
#         """search in plants by name"""
#         getData = nameSerializer(data=request.data)
#         if getData.is_valid():
#
#             sort = getData.data['sort']
#             pagination = getData.data['pagination']
#
#             plants = Plant.objects.filter(name__contains = getData.data['name'])
#
#             if (sort is not None):
#                 plants = sorting(plants, sort['kind'], sort['order'])
#
#             if(pagination is not None):
#                 data['pageCount'] = ceil(plants.count()/pagination['count'])
#                 plants = paginator(plants, pagination['count'], pagination['page'])
#
#             serializer = PlantSerializer(plants, many=True)
#
#             data['data'] = serializer.data
#
#             return Response(data)
#         return Response(getData.errors, status=400)
#
# class plantsByPrice(APIView):
#     def post(self, request, format=None):
#         """search in plants by price"""
#         getData = priceSerializer(data=request.data)
#         if getData.is_valid():
#
#             data = {'pageCount':1}
#
#             sort = getData.data['sort']
#             pagination = getData.data['pagination']
#
#             lower = getData.data['lower']
#             higher = getData.data['higher']
#
#             if (lower is not None and higher is not None):
#                 if (higher == -1 and lower == 0):
#                     plants = Plant.objects.all()
#                 elif (higher == -1):
#                     plants = Plant.objects.filter(price__gte = lower)
#                 elif (lower == 0):
#                     plants = Plant.objects.filter(price__lte = higher)
#                 else:
#                     plants = Plant.objects.filter(price__gt = lower, price__lt= higher)
#
#             if (sort is not None):
#                 plants = sorting(plants, sort['kind'], sort['order'])
#
#             if(pagination is not None):
#                 data['pageCount'] = ceil(plants.count()/pagination['count'])
#                 plants = paginator(plants, pagination['count'], pagination['page'])
#
#             serializer = PlantSerializer(plants, many=True)
#
#             data['data'] = serializer.data
#
#             return Response(data)
#         return Response(getData.errors, status=400)
#
# class plantsByEnvironment(APIView):
#     def post(self, request, format=None):
#         """search in plants by environment"""
#         getData = environmentSerializer(data=request.data)
#         if getData.is_valid():
#
#             data = {'pageCount':1}
#
#             sort = getData.data['sort']
#             pagination = getData.data['pagination']
#
#             plants = Plant.objects.filter(environment = getData.data['environment'])
#
#             if (sort is not None):
#                 plants = sorting(plants, sort['kind'], sort['order'])
#
#             if(pagination is not None):
#                 data['pageCount'] = ceil(plants.count()/pagination['count'])
#                 plants = paginator(plants, pagination['count'], pagination['page'])
#
#             serializer = PlantSerializer(plants, many=True)
#
#             data['data'] = serializer.data
#
#             return Response(data)
#         return Response(getData.errors, status=400)
#
# class plantsByWater(APIView):
#     def post(self, request, format=None):
#         """search in plants by water"""
#         getData = waterSerializer(data=request.data)
#         if getData.is_valid():
#
#             data = {'pageCount':1}
#
#             sort = getData.data['sort']
#             pagination = getData.data['pagination']
#
#             plants = Plant.objects.filter(water = getData.data['water'])
#
#             if (sort is not None):
#                 plants = sorting(plants, sort['kind'], sort['order'])
#
#             if(pagination is not None):
#                 data['pageCount'] = ceil(plants.count()/pagination['count'])
#                 plants = paginator(plants, pagination['count'], pagination['page'])
#
#             serializer = PlantSerializer(plants, many=True)
#
#             data['data'] = serializer.data
#
#             return Response(data)
#         return Response(getData.errors, status=400)
#
# class plantsByLight(APIView):
#     def post(self, request, format=None):
#         """search in plants by light"""
#         getData = lightSerializer(data=request.data)
#         if getData.is_valid():
#
#             data = {'pageCount':1}
#
#             sort = getData.data['sort']
#             pagination = getData.data['pagination']
#
#             plants = Plant.objects.filter(light = getData.data['light'])
#
#             if (sort is not None):
#                 plants = sorting(plants, sort['kind'], sort['order'])
#
#             if(pagination is not None):
#                 data['pageCount'] = ceil(plants.count()/pagination['count'])
#                 plants = paginator(plants, pagination['count'], pagination['page'])
#
#             serializer = PlantSerializer(plants, many=True)
#
#             data['data'] = serializer.data
#
#             return Response(data)
#         return Response(getData.errors, status=400)
#
# class plantsByGrowthRate(APIView):
#     def post(self, request, format=None):
#         """search in plants by growth rate"""
#         getData = growthRateSerializer(data=request.data)
#         if getData.is_valid():
#
#             data = {'pageCount':1}
#
#             sort = getData.data['sort']
#             pagination = getData.data['pagination']
#
#             plants = Plant.objects.filter(growthRate = getData.data['growthRate'])
#
#             if (sort is not None):
#                 plants = sorting(plants, sort['kind'], sort['order'])
#
#             if(pagination is not None):
#                 data['pageCount'] = ceil(plants.count()/pagination['count'])
#                 plants = paginator(plants, pagination['count'], pagination['page'])
#
#             serializer = PlantSerializer(plants, many=True)
#
#             data['data'] = serializer.data
#
#             return Response(data)
#         return Response(getData.errors, status=400)
#
# class plantsByTags(APIView):
#     def post(self, request, format=None):
#         """search in plants by tags"""
#         getData = tagsSerializer(data=request.data)
#         if getData.is_valid():
#
#             data = {'pageCount':1}
#
#             sort = getData.data['sort']
#             pagination = getData.data['pagination']
#
#             plants = Plant.objects.all()
#             for tag in tags:
#                 tag = findTag(tag)
#                 if tag != None:
#                     plants = plants.filter(tags__in=[tag.id])
#
#             if (sort is not None):
#                 plants = sorting(plants, sort['kind'], sort['order'])
#
#             if(pagination is not None):
#                 data['pageCount'] = ceil(plants.count()/pagination['count'])
#                 plants = paginator(plants, pagination['count'], pagination['page'])
#
#             serializer = PlantSerializer(plants, many=True)
#
#             data['data'] = serializer.data
#
#             return Response(data)
#         return Response(getData.errors, status=400)
#
# # advance
# class plantsAdvanceSearch(APIView):
#     def post(self, request, format=None):
#         """advance search in plants"""
#         getData = plantAdvanceSerializer(data=request.data)
#         if getData.is_valid():
#
#             data = {'pageCount':1}
#
#             plants = Plant.objects.all()
#             sort = getData.data['sort']
#             pagination = getData.data['pagination']
#
#             _name = getData.data['name']
#             price = getData.data['price']
#             _environment = getData.data['environment']
#             _water = getData.data['water']
#             _light = getData.data['light']
#             _growthRate = getData.data['growthRate']
#             tags = getData.data['tags']
#             onlyAvailables = getData['onlyAvailables']
#
#             if (onlyAvailables is not None):
#                 plants = plants.filter(count__gt = 0)
#
#             if (_name is not None):
#                 plants = plants.filter(name__contains = _name)
#
#             if (_environment is not None):
#                 plants = plants.filter(environment = _environment)
#
#             if (_water is not None):
#                 plants = plants.filter(water = _water)
#
#             if (_light is not None):
#                 plants = plants.filter(light = _light)
#
#             if (_growthRate is not None):
#                 plants = plants.filter(growthRate = _growthRate)
#
#             for tag in tags:
#                 tag = findTag(tag)
#                 if tag is not None:
#                     plants = plants.filter(tags__in=[tag.id])
#
#             serializer = PlantSerializer(plants, many=True)
#             li = serializer.data
#
#             min_price = min(li, key=lambda x:x['price'])
#             max_price = max(li, key=lambda x:x['price'])
#
#             if (price is not None):
#                 lower = price['lower']
#                 higher = price['higher']
#                 if (lower is not None and higher is not None):
#                     if (higher == -1 and lower == 0):
#                         pass
#                     elif (higher == -1):
#                         li = list(filter(lambda x:x['price'] >= lower, li))
#                     elif (lower == 0):
#                         li = list(filter(lambda x:x['price'] <= higher, li))
#                     else:
#                         li = list(filter(lambda x:x['price'] >= lower and x['price'] <= higher, li))
#
#             data['priceBound'] = {'lower':min_price['price'], 'higher':max_price['price']}
#
#             if (sort is not None):
#                 if (sort['kind'] is not None and sort['order'] is not None):
#                     li = sorting(li, sort['kind'], sort['order'])
#
#             if(pagination is not None):
#                 if (pagination['count'] is not None and pagination['page'] is not None):
#                     data['pageCount'] = ceil(len(li)/pagination['count'])
#                     li = paginator(li, pagination['count'], pagination['page'])
#
#             data['data'] = li
#
#             return Response(data)
#         return Response(getData.errors, status=400)
#
# # filters for tools
# class toolsByName(APIView):
#     def post(self, request, format=None):
#         """search in tools by name"""
#         getData = nameSerializer(data=request.data)
#         if getData.is_valid():
#
#             data = {'pageCount':1}
#
#             sort = getData.data['sort']
#             pagination = getData.data['pagination']
#
#             tools = Tool.objects.filter(name__contains = getData.data['name'])
#
#             if (sort is not None):
#                 tools = sorting(tools, sort['kind'], sort['order'])
#
#             if(pagination is not None):
#                 data['pageCount'] = ceil(tools.count()/pagination['count'])
#                 tools = paginator(tools, pagination['count'], pagination['page'])
#
#             serializer = ToolSerializer(tools, many=True)
#
#             data['data'] = serializer.data
#
#             return Response(data)
#         return Response(getData.errors, status=400)
#
# class toolsByPrice(APIView):
#     def post(self, request, format=None):
#         """search in tools by price"""
#         getData = priceSerializer(data=request.data)
#         if getData.is_valid():
#
#             data = {'pageCount':1}
#
#             sort = getData.data['sort']
#             pagination = getData.data['pagination']
#
#             lower = getData.data['lower']
#             higher = getData.data['higher']
#
#             if( lower is not None and higher is not None):
#                 if (higher == -1 and lower == 0):
#                     tools = Tool.objects.all()
#                 elif (higher == -1):
#                     tools = Tool.objects.filter(price__gte = lower)
#                 elif (lower == 0):
#                     tools = Tool.objects.filter(price__lte = higher)
#                 else:
#                     tools = Tool.objects.filter(price__gt = lower, price__lt= higher)
#
#             if (sort is not None):
#                 tools = sorting(tools, sort['kind'], sort['order'])
#
#             if(pagination is not None):
#                 data['pageCount'] = ceil(tools.count()/pagination['count'])
#                 tools = paginator(tools, pagination['count'], pagination['page'])
#
#             serializer = ToolSerializer(tools, many=True)
#
#             data['data'] = serializer.data
#
#             return Response(data)
#         return Response(getData.errors, status=400)
#
# class toolsByTags(APIView):
#     def post(self, request, format=None):
#         """search in tools by tags"""
#         getData = tagsSerializer(data=request.data)
#         if getData.is_valid():
#
#             data = {'pageCount':1}
#
#             sort = getData.data['sort']
#             pagination = getData.data['pagination']
#
#             tools = Tool.objects.all()
#             for tag in tags:
#                 tag = findTag(tag)
#                 if tag != None:
#                     tools = tools.filter(tags__in=[tag.id])
#
#             if (sort is not None):
#                 tools = sorting(tools, sort['kind'], sort['order'])
#
#             if(pagination is not None):
#                 data['pageCount'] = ceil(tools.count()/pagination['count'])
#                 tools = paginator(tools, pagination['count'], pagination['page'])
#
#             serializer = ToolSerializer(tools, many=True)
#
#             data['data'] = serializer.data
#
#             return Response(data)
#         return Response(getData.errors, status=400)
#
# # advance
# class toolsAdvanceSearch(APIView):
#     def post(self, request, format=None):
#         """advance search in tools"""
#         getData = toolAdvanceSerializer(data=request.data)
#         if getData.is_valid():
#
#             data = {'pageCount':1}
#
#             tools = Tool.objects.all()
#
#             sort = getData.data['sort']
#             pagination = getData.data['pagination']
#
#             _name = getData.data['name']
#             price = getData.data['price']
#             tags = getData.data['tags']
#             onlyAvailables = getData['onlyAvailables']
#
#             if (onlyAvailables is not None):
#                 tools = tools.filter(count__gt = 0)
#
#             if (_name is not None):
#                 tools = tools.filter(name__contains = _name)
#
#             for tag in tags:
#                 tag = findTag(tag)
#                 if tag is not None:
#                     tools = tools.filter(tags__in=[tag.id])
#
#             serializer = ToolSerializer(tools, many=True)
#             li = serializer.data
#
#             min_price = min(li, key=lambda x:x['price'])
#             max_price = max(li, key=lambda x:x['price'])
#
#             if (price is not None):
#                 lower = price['lower']
#                 higher = price['higher']
#                 if (lower is not None and higher is not None):
#                     if (higher == -1 and lower == 0):
#                         pass
#                     elif (higher == -1):
#                         li = list(filter(lambda x:x['price'] >= lower, li))
#                     elif (lower == 0):
#                         li = list(filter(lambda x:x['price'] <= higher, li))
#                     else:
#                         li = list(filter(lambda x:x['price'] >= lower and x['price'] <= higher, li))
#
#             data['priceBound'] = {'lower':min_price['price'], 'higher':max_price['price']}
#
#             if (sort is not None):
#                 if (sort['kind'] is not None and sort['order'] is not None):
#                     li = sorting(li, sort['kind'], sort['order'])
#
#             if(pagination is not None):
#                 if (pagination['count'] is not None and pagination['page'] is not None):
#                     data['pageCount'] = ceil(len(li)/pagination['count'])
#                     li = paginator(li, pagination['count'], pagination['page'])
#
#             data['data'] = li
#
#             return Response(data)
#         return Response(getData.errors, status=400)
#
# # plants sorting
# class plantsSort(APIView):
#     def post(self, request, format=None):
#         """plantsSort"""
#         getData = sortSerializer(data=request.data)
#         if getData.is_valid():
#             plants = Plant.objects.all()
#             kind = getData.data['kind']
#             order = getData.data['order']
#             if (kind is not None and order is not None):
#                 plants = sorting(plants,kind,order)
#             serializer = PlantSerializer(plants, many=True)
#             return Response(serializer.data)
#         return Response(getData.errors, status=400)
#
# # tools sorting
# class toolsSort(APIView):
#     def post(self, request, format=None):
#         """toolsSort"""
#         getData = sortSerializer(data=request.data)
#         if getData.is_valid():
#             tools = Tool.objects.all()
#             kind = getData.data['kind']
#             order = getData.data['order']
#             if (kind is not None and order is not None):
#                 tools = sorting(tools,kind,order)
#             serializer = ToolSerializer(tools, many=True)
#             return Response(serializer.data)
#         return Response(getData.errors, status=400)
#
# # plants pagination
# class plantsPagination(APIView):
#     def post(self, request, format=None):
#         """plantsPagination"""
#         getData = paginatorSerializer(data=request.data)
#         if getData.is_valid():
#             data = {}
#             plants = Plant.objects.all()
#             count = getData.data['count']
#             page = getData.data['page']
#             if (count is not None and page is not None):
#                 data['pageCount'] = ceil(tools.count()/count)
#                 plants = paginator(plants, count, page)
#             serializer = PlantSerializer(plants, many=True)
#             data['data'] = serializer.data
#             return Response(data)
#         return Response(getData.errors, status=400)
#
# # tools pagination
# class toolsPagination(APIView):
#     def post(self, request, format=None):
#         """toolsPagination"""
#         getData = paginatorSerializer(data=request.data)
#         if getData.is_valid():
#             data = {}
#             tools = Tool.objects.all()
#             count = getData.data['count']
#             page = getData.data['page']
#             if (count is not None and page is not None):
#                 data['pageCount'] = ceil(tools.count()/count)
#                 tools = paginator(tools, count, page)
#             serializer = ToolSerializer(tools, many=True)
#             data['data'] = serializer.data
#             return Response(data)
#         return Response(getData.errors, status=400)
#
# # all products pagination
# class allPagination(APIView):
#     def post(self, request, format=None):
#         """allPagination"""
#         getData = paginatorSerializer(data=request.data)
#         if getData.is_valid():
#             data = {}
#             plants = Plant.objects.all()
#             tools = Tool.objects.all()
#             count = getData.data['count']
#             page = getData.data['page']
#             if (count is not None and page is not None):
#                 data['pageCount'] = ceil((tools.count() + plants.count())/count)
#             plantsSerializer = PlantSerializer(plants, many=True)
#             toolsSerializer = ToolSerializer(tools, many=True)
#             li = plantsSerializer.data + toolsSerializer.data
#             li = sorted(li, key= lambda x:x['price'], reverse=True)
#             li = paginator(li, count, page)
#             data['data'] = li
#             return Response(data)
#         return Response(getData.errors, status=400)
#
# # all products advance search
# class allAdvanceSearch(APIView):
#     def post(self, request, format=None):
#         """advance search in all products"""
#         getData = toolAdvanceSerializer(data=request.data)
#         if getData.is_valid():
#
#             data = {'pageCount':1}
#
#             plants = Plant.objects.all()
#             tools = Tool.objects.all()
#
#             sort = getData.data['sort']
#             pagination = getData.data['pagination']
#
#             _name = getData.data['name']
#             price = getData.data['price']
#             onlyAvailables = getData['onlyAvailables']
#
#             if (onlyAvailables is not None):
#                 plants = plants.filter(count__gt = 0)
#                 tools = tools.filter(count__gt = 0)
#
#             if (_name is not None):
#                 plants = plants.filter(name__contains = _name)
#                 tools = tools.filter(name__contains = _name)
#
#             plantsSerializer = PlantSerializer(plants, many=True)
#             toolsSerializer = ToolSerializer(tools, many=True)
#             li = plantsSerializer.data + toolsSerializer.data
#
#             min_price = min(li, key=lambda x:x['price'])
#             max_price = max(li, key=lambda x:x['price'])
#
#             if (price is not None):
#                 lower = price['lower']
#                 higher = price['higher']
#                 if (lower is not None and higher is not None):
#                     if (higher == -1 and lower == 0):
#                         pass
#                     elif (higher == -1):
#                         li = list(filter(lambda x:x['price'] >= lower, li))
#                     elif (lower == 0):
#                         li = list(filter(lambda x:x['price'] <= higher, li))
#                     else:
#                         li = list(filter(lambda x:x['price'] >= lower and x['price'] <= higher, li))
#
#             data['priceBound'] = {'lower':min_price['price'], 'higher':max_price['price']}
#
#             if (sort is not None):
#                 if (sort['kind'] is not None and sort['order'] is not None):
#                     li = sorting(li, sort['kind'], sort['order'])
#             else:
#                 li = sorting(li, "name", "ASC")
#
#             if(pagination is not None):
#                 if (pagination['count'] is not None and pagination['page'] is not None):
#                     data['pageCount'] = ceil(len(li)/pagination['count'])
#                     li = paginator(li, pagination['count'], pagination['page'])
#
#             data['data'] = li
#
#             return Response(data)
#         return Response(getData.errors, status=400)