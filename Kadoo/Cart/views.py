from django.db.models import ProtectedError
from rest_framework.decorators import api_view

from django.shortcuts import render
from rest_framework import response, status
from rest_framework.views import APIView
from Backend.models import Plant, Tool
from Cart.models import OrderModel, PlantCartModel, ToolCartModel

from Cart.serializers import CartItemIdSerializer, CartItemSerializer, PlantCartSerializer, PlantWithCountCartSerializer, ToolCartSerializer, DesicriptionSerializer, ToolWithCountCartSerializer

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        '(post) Add A Plnat To Cart (*id,count=1,decription)':'/add-plant-to-cart/',
        '(post) Add A Tool To Cart (*id,count=1,decription)':'/add-tool-to-cart/',
        '(get) Get All Plants of User':'/user-all-plants/',
        '(get) Get All Tools of User':'/user-all-tools/',
        '(get) Get All Unapproved Plants of User (in Cart)':'/user-unapproved-plants-cart/',
        '(get) Get All Unapproved Tools of User (in Cart)':'/user-unapproved-tools-cart/',
        '(get) Get All Unapproved Plants of User with Count (in Cart)':'/user-unapproved-plants-cart-count/',
        '(get) Get All Unapproved Tools of User with Count (in Cart)':'/user-unapproved-tools-cart-count/',
        '(get) Get All Approved Plants of User':'/user-approved-plants-cart/',
        '(get) Get All Approved Tools of User':'/user-approved-tools-cart/',
        '(get) Get Price Of The Cart':'/user-price-cart/',
        '(get) Get Count Of Items In The Cart':'/user-count-cart/',
        '(post) Update A Plant in Cart (*id,count=1,decription)':'/update-plant-cart/',
        '(post) Update A Tool in Cart (*id,count=1,decription)':'/update-tool-cart/',
        '(delete) Delete A Plant in Cart (*id)':'/delete-plant-cart/',
        '(delete) Delete A Tool in Cart (*id)':'/delete-tool-cart/',
        '(delete) Delete All Plants in Cart':'/delete-all-plant-cart/',
        '(delete) Delete All Tools in Cart':'/delete-all-tool-cart/',
        '(post) Approve All in Cart':'/approve-all-cart/',
    }
    return response.Response(api_urls)

#######################
#------------ CRUD Cart
#######################

#------- CREATE
###############

#Create Plant
class AddPlantToCart(APIView):
 def post(self, request, format='json'):
  serializer = CartItemSerializer(data=request.data)
  if serializer.is_valid():
    #Get All Data
    if request.user.is_anonymous:
      return response.Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
    userToAdd = request.user
    if Plant.objects.filter(id=serializer.data["id"]).exists() == False:
      return response.Response("This plant does NOT Exist!", status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    PlantToAdd = Plant.objects.get(id=serializer.data["id"])
    PlantToAddCount = serializer.data["count"]
    PlantToAddDescription = serializer.data["description"]
    #Check if it Exists
    if PlantCartModel.objects.filter(user=userToAdd, plant_item=PlantToAdd, is_approved=False).exists():
      return response.Response("This Plant is Alraedy On The Cart", status=status.HTTP_400_BAD_REQUEST)
    #Make Cart Plant Item
    PlantCartItem = PlantCartModel.objects.create(user=userToAdd, plant_item=PlantToAdd, plant_count=PlantToAddCount, description=PlantToAddDescription)
    #Save Plant Item
    PlantCartItem.save()
    if PlantCartItem:
      json = serializer.data
      return response.Response(json, status=status.HTTP_201_CREATED)
    return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  return response.Response("Data is Not Valid!", status=status.HTTP_400_BAD_REQUEST)

#Create Tool
class AddToolToCart(APIView):
 def post(self, request, format='json'):
  serializer = CartItemSerializer(data=request.data)
  if serializer.is_valid():
   #Get All Data
   if request.user.is_anonymous:
    return response.Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
   userToAdd = request.user
   if Tool.objects.filter(id=serializer.data["id"]).exists() == False:
     return response.Response("This Tool does NOT Exist!", status=status.HTTP_422_UNPROCESSABLE_ENTITY)
   ToolToAdd = Tool.objects.get(id=serializer.data["id"])
   ToolToAddCount = serializer.data["count"]
   ToolToAddDescription = serializer.data["description"]
   #Check if it Exists
   if ToolCartModel.objects.filter(user=userToAdd, tool_item=ToolToAdd, is_approved=False).exists():
    return response.Response("This Tool is Alraedy On The Cart", status=status.HTTP_400_BAD_REQUEST)
   #Make Cart Plant Item
   ToolCartItem = ToolCartModel.objects.create(user=userToAdd, tool_item=ToolToAdd, tool_count=ToolToAddCount, description=ToolToAddDescription)
   #Save Plant Item
   ToolCartItem.save()
   if ToolCartItem:
    json = serializer.data
    return response.Response(json, status=status.HTTP_201_CREATED)
   return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#------- READ
###############

#Read ALL Plants
class GetAllPlantsCart(APIView):
 def get(self, request, format='json'):
  if request.user.is_anonymous:
    return response.Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
  userToGetCart = request.user
  PlantsCartItems = PlantCartModel.objects.filter(user=userToGetCart)
  if PlantsCartItems.count == 0:
    return response.Response("No bought item nor in cart!", status=status.HTTP_200_OK);
  serializer = PlantCartSerializer(PlantsCartItems, many=True)
  return response.Response(serializer.data, status=status.HTTP_200_OK)

#Read All Tools
class GetAllToolsCart(APIView):
 def get(self, request, format='json'):
  if request.user.is_anonymous:
    return response.Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
  userToGetCart = request.user
  ToolsCartItems = ToolCartModel.objects.filter(user=userToGetCart)
  if ToolsCartItems.count == 0:
    return response.Response("No bought item nor in cart!", status=status.HTTP_200_OK);
  serializer = ToolCartSerializer(ToolsCartItems, many=True)
  return response.Response(serializer.data, status=status.HTTP_200_OK)

#Read ALL Unapproved Plants
class GetUnapprovedPlantsCart(APIView):
 def get(self, request, format='json'):
  if request.user.is_anonymous:
    return response.Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
  userToGetCart = request.user
  PlantsCartItems = PlantCartModel.objects.filter(user=userToGetCart, is_approved=False)
  if PlantsCartItems.count == 0:
    return response.Response("There is No Plant in Cart!", status=status.HTTP_404_NOT_FOUND);
  serializer = PlantCartSerializer(PlantsCartItems, many=True)
  return response.Response(serializer.data, status=status.HTTP_200_OK)

#Read All Unapproved Tools
class GetUnapprovedToolsCart(APIView):
 def get(self, request, format='json'):
  if request.user.is_anonymous:
    return response.Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
  userToGetCart = request.user
  ToolsCartItems = ToolCartModel.objects.filter(user=userToGetCart, is_approved=False)
  if ToolsCartItems.count == 0:
    return response.Response("There is No Tool in Cart!", status=status.HTTP_404_NOT_FOUND);
  serializer = ToolCartSerializer(ToolsCartItems, many=True)
  return response.Response(serializer.data, status=status.HTTP_200_OK)

#Read ALL Unapproved Plants Plant Format
class GetUnapprovedPlantsCartWithCount(APIView):
 def get(self, request, format='json'):
  if request.user.is_anonymous:
    return response.Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
  userToGetCart = request.user
  PlantsCartItems = PlantCartModel.objects.filter(user=userToGetCart, is_approved=False).values('plant_item')
  PlantsItems = Plant.objects.filter(id__in = PlantsCartItems).order_by('name')
  PlantsCountItems = PlantCartModel.objects.filter(user=userToGetCart, is_approved=False).order_by('plant_item__name').values('plant_count')
  index = 0
  for PlantItem in PlantsItems:
    countitem = PlantsCountItems[index]
    print(countitem)
    PlantItem.count = countitem['plant_count']
    index = index + 1
  if PlantsCartItems.count == 0:
    return response.Response("There is No Plant in Cart!", status=status.HTTP_404_NOT_FOUND);
  serializer = PlantWithCountCartSerializer(PlantsItems, many=True)
  return response.Response(serializer.data, status=status.HTTP_200_OK)

#Read All Unapproved Tools Tool Format
class GetUnapprovedToolsCartWithCount(APIView):
 def get(self, request, format='json'):
  if request.user.is_anonymous:
    return response.Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
  userToGetCart = request.user
  ToolsCartItems = ToolCartModel.objects.filter(user=userToGetCart, is_approved=False).values('tool_item')
  ToolsItems = Tool.objects.filter(id__in = ToolsCartItems).order_by('name')
  ToolsCountItems = ToolCartModel.objects.filter(user=userToGetCart, is_approved=False).order_by('tool_item__name').values('tool_count')
  
  index = 0
  for ToolItem in ToolsItems:
    countitem = ToolsCountItems[index]
    print(countitem)
    ToolItem.count = countitem['tool_count']
    index = index + 1
  if ToolsCountItems.count == 0:
    return response.Response("There is No Plant in Cart!", status=status.HTTP_404_NOT_FOUND);
  serializer = ToolWithCountCartSerializer(ToolsItems, many=True)
  return response.Response(serializer.data, status=status.HTTP_200_OK)

#Read ALL Approved Plants
class GetApprovedPlantsCart(APIView):
 def get(self, request, format='json'):
  if request.user.is_anonymous:
    return response.Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
  userToGetCart = request.user
  PlantsCartItems = PlantCartModel.objects.filter(user=userToGetCart, is_approved=True)
  if PlantsCartItems.count == 0:
    return response.Response("No bought plant up to now!", status=status.HTTP_200_OK);
  serializer = PlantCartSerializer(PlantsCartItems, many=True)
  return response.Response(serializer.data, status=status.HTTP_200_OK)

#Read All Approved Tools
class GetApprovedToolsCart(APIView):
 def get(self, request, format='json'):
  if request.user.is_anonymous:
    return response.Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
  userToGetCart = request.user
  ToolsCartItems = ToolCartModel.objects.filter(user=userToGetCart, is_approved=True)
  if ToolsCartItems.count == 0:
    return response.Response("No bought tool up to now!", status=status.HTTP_200_OK);
  serializer = ToolCartSerializer(ToolsCartItems, many=True)
  return response.Response(serializer.data, status=status.HTTP_200_OK)

#Raed The Price
class GetPriceCart(APIView):
 def get(self, request, format='json'):
  if request.user.is_anonymous:
    return response.Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
  price = 0
  userToGetCart = request.user
  PlantsCartItems = PlantCartModel.objects.filter(user=userToGetCart, is_approved=False)
  ToolsCartItems = ToolCartModel.objects.filter(user=userToGetCart, is_approved=False)
  
  for PlantItem in PlantsCartItems:
    plant = PlantItem.plant_item
    count =  PlantItem.plant_count
    price = price + (count * plant.price)
  for ToolItem in ToolsCartItems:
    tool = ToolItem.tool_item
    count =  ToolItem.tool_count
    price = price + (count * tool.price)
  
  return response.Response(price, status=status.HTTP_200_OK)

#Raed The Count
class GetCountCart(APIView):
 def get(self, request, format='json'):
  if request.user.is_anonymous:
    return response.Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
  count = 0
  userToGetCart = request.user
  count += PlantCartModel.objects.filter(user=userToGetCart, is_approved=False).count()
  count += ToolCartModel.objects.filter(user=userToGetCart, is_approved=False).count()
  return response.Response(count, status=status.HTTP_200_OK)

#------- UPDATE
###############

#Update Plant
class UpdatePlantToCart(APIView):
 def post(self, request, format='json'):
  serializer = CartItemSerializer(data=request.data)
  if serializer.is_valid():
   #Get All Data
   if request.user.is_anonymous:
    return response.Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
   userToUpdate = request.user
   if Plant.objects.filter(id=serializer.data["id"]).exists() == False:
     return response.Response("This plant does NOT Exist!", status=status.HTTP_422_UNPROCESSABLE_ENTITY)
   PlantToUpdate = Plant.objects.get(id=serializer.data["id"])
   PlantToUpdateCount = serializer.data["count"]
   PlantToUpdateDescription = serializer.data["description"]
   #Make Cart Plant Item
   if PlantCartModel.objects.filter(user=userToUpdate, plant_item=PlantToUpdate, is_approved=False).exists() == False:
     return response.Response("This plant does NOT Exist in cart!", status=status.HTTP_404_NOT_FOUND)
   PlantCartItem = PlantCartModel.objects.get(user=userToUpdate, plant_item=PlantToUpdate, is_approved=False)
   PlantCartItem.plant_count = PlantToUpdateCount
   PlantCartItem.description = PlantToUpdateDescription
   #Save Plant Item
   PlantCartItem.save()
   if PlantCartItem:
    json = serializer.data
    return response.Response(json, status=status.HTTP_201_CREATED)
   return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  return response.Response("Data is Not Valid!", status=status.HTTP_400_BAD_REQUEST)

#Update Tool
class UpdateToolToCart(APIView):
 def post(self, request, format='json'):
  serializer = CartItemSerializer(data=request.data)
  if serializer.is_valid():
   #Get All Data
   if request.user.is_anonymous:
    return response.Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
   userToUpdate = request.user
   if Tool.objects.filter(id=serializer.data["id"]).exists() == False:
     return response.Response("This Tool does NOT Exist!", status=status.HTTP_422_UNPROCESSABLE_ENTITY)
   ToolToUpdate = Tool.objects.get(id=serializer.data["id"])
   ToolToUpdateCount = serializer.data["count"]
   ToolToUpdateDescription = serializer.data["description"]
   #Make Cart Plant Item
   if ToolCartModel.objects.filter(user=userToUpdate, tool_item=ToolToUpdate, is_approved=False).exists() == False:
     return response.Response("This Tool does NOT Exist in cart!", status=status.HTTP_404_NOT_FOUND)
   ToolCartItem = ToolCartModel.objects.get(user=userToUpdate, tool_item=ToolToUpdate, is_approved=False)
   ToolCartItem.tool_count = ToolToUpdateCount
   ToolCartItem.description = ToolToUpdateDescription
   #Save Plant Item
   ToolCartItem.save()
   if ToolCartItem:
    json = serializer.data
    return response.Response(json, status=status.HTTP_201_CREATED)
   return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  return response.Response("Data is Not Valid!", status=status.HTTP_400_BAD_REQUEST)

#------- DELETE
###############

#Delete Plant
class RemovePlantFromCart(APIView):
 def delete(self, request, format='json'):
  serializer = CartItemIdSerializer(data=request.data)
  if serializer.is_valid():
   #Get Plant Data
   if request.user.is_anonymous:
    return response.Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
   UserToDeleteItem = request.user
   if Plant.objects.filter(id=serializer.data["id"]).exists() == False:
     return response.Response("This plant does NOT Exist!", status=status.HTTP_422_UNPROCESSABLE_ENTITY)
   PlantToRemove = Plant.objects.get(id=serializer.data["id"])
   #Make Cart Plant Item
   try:
    PlantCartModel.objects.filter(user=UserToDeleteItem, plant_item=PlantToRemove, is_approved=False).delete()
   except ProtectedError:
    return response.Response("Can NOT Remove This Plant! this may does NOT Exist", status=status.HTTP_400_BAD_REQUEST)
   return response.Response("Plant removed from the cart.",  status=status.HTTP_200_OK)
  return response.Response("Data is Not Valid!", status=status.HTTP_400_BAD_REQUEST)

#Delete Tool
class RemoveToolFromCart(APIView):
 def delete(self, request, format='json'):
  serializer = CartItemIdSerializer(data=request.data)
  if serializer.is_valid():
   #Get Plant Data
   if request.user.is_anonymous:
    return response.Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
   UserToDeleteItem = request.user
   if Plant.objects.filter(id=serializer.data["id"]).exists() == False:
     return response.Response("This plant does NOT Exist!", status=status.HTTP_422_UNPROCESSABLE_ENTITY)
   ToolToRemove = Tool.objects.get(id=serializer.data["id"])
   #Make Cart Plant Item
   try:
    ToolCartModel.objects.filter(user=UserToDeleteItem, tool_item=ToolToRemove, is_approved=False).delete()
   except ProtectedError:
    return response.Response("Can NOT Remove This Tool", status=status.HTTP_400_BAD_REQUEST)
   return response.Response("Tool removed from the cart.",  status=status.HTTP_200_OK)
  return response.Response("Data is Not Valid!", status=status.HTTP_400_BAD_REQUEST)

#Delte All Plants
class RemoveAllPlantsFromCart(APIView):
 def delete(self, request, format='json'):
   if request.user.is_anonymous:
    return response.Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
   UserToDeleteItem = request.user
   #Delete All
   try:
    PlantCartModel.objects.filter(user=UserToDeleteItem, is_approved=False).delete()
   except ProtectedError:
    return response.Response("Can NOT Delete All", status=status.HTTP_400_BAD_REQUEST)
   return response.Response("Plants Removed",  status=status.HTTP_200_OK)

#Delete All Tools
class RemoveAllToolsFromCart(APIView):
 def delete(self, request, format='json'):
   if request.user.is_anonymous:
    return response.Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
   UserToDeleteItem = request.user
   #Delete All
   try:
    ToolCartModel.objects.filter(user=UserToDeleteItem, is_approved=False).delete()
   except ProtectedError:
    return response.Response("Can NOT Delete All", status=status.HTTP_400_BAD_REQUEST)
   return response.Response("Tools Removed",  status=status.HTTP_200_OK)

#Checkout Plant Cart
class ApproveAllInCart(APIView):
 def post(self, request, format='json'):
   serializer = DesicriptionSerializer(data=request.data)
   if serializer.is_valid():
    if request.user.is_anonymous:
      return response.Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
    UserToApproveCart = request.user
    PlantsToApprove = PlantCartModel.objects.filter(user=UserToApproveCart, is_approved=False)
    ToolsToApprove = ToolCartModel.objects.filter(user=UserToApproveCart, is_approved=False)
    if PlantsToApprove.count == 0 and ToolsToApprove.count == 0:
     return response.Response("Cart is Empthy!", status=status.HTTP_400_BAD_REQUEST)
    OrderDescription = serializer.data["description"]
    price = 0
    for PlantItem in PlantsToApprove:
      plant = PlantItem.plant_item
      count =  PlantItem.plant_count
      price = price + (count * plant.price)
    for ToolItem in ToolsToApprove:
      tool = ToolItem.tool_item
      count =  ToolItem.tool_count
      price = price + (count * tool.price)
    #Make Cart Plant Item
    NewOrder = OrderModel.objects.create(user=UserToApproveCart, total_price=price, description=OrderDescription)
    NewOrder.order_plants.set(PlantsToApprove)
    NewOrder.order_tools.set(ToolsToApprove)
    NewOrder.save()
    if NewOrder:
     PlantCartModel.objects.filter(user=UserToApproveCart, is_approved=False).update(is_approved=True)
     ToolCartModel.objects.filter(user=UserToApproveCart, is_approved=False).update(is_approved=True)
     json = serializer.data
     return response.Response(json, status=status.HTTP_201_CREATED)
   return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
