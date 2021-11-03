from django.db.models.deletion import ProtectedError
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from Specialist.models import Specialist, SpecilistFields
from django.contrib.auth.models import Group

from Specialist.serializers import CustomSpecialistSerializer, SpecialistCompeleteInfoSerializer, SpecialistIdSerializer
from Users.models import NewUser
from Users.serializers import UserSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        '(post) Register A User (*email,*username,*firstname,*lastname,*password)':'/register/',
        '(get) Get All Specialists Primary Info':'/all-primary/',
        '(get) Get All Specialists Secondary Info':'/all-secondary/',
        '(get) Get This Specialist Primary Info':'/primary/',
        '(get) Get This Specialist Secondary Info':'/secondary/',
        '(get) Get Specialist Secondary Info By Id':'/secondary/<str:pk>/',
        '(post) Update this User Secondary Info (id_code, birth_date, degree, major, phone_number, about,address,is_online, rate)':'/update-secondary/',
        '(delete) Delete Specialist By Id (*id)':'/delete/',
    }
    return Response(api_urls)


#######################
#------------ CRUD Specialist
#######################


#------- CREATE
###############

#Create Specialists
class CustomSpecialistCreate(APIView):
    permission_classes = [AllowAny]
    def post(self, request, format='json'):
        serializer = CustomSpecialistSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                Specialist_group = Group.objects.get(name='my_group_name') 
                Specialist_group.user_set.add(user)
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#------- READ
###############

#Get All Specialists Primary Info
class GetAllSpecialistPrimaryInfo(APIView):
 def get(self, request, format='json'):
   Specialists = Specialist.objects.all()
   serializer = UserSerializer(Specialists, many=True)
   return Response(serializer.data)

#Get All Specialists Secondary Info
class GetAllSpecialistSecondaryInfo(APIView):
 def get(self, request, format='json'):
   Specialists = SpecilistFields.objects.all()
   serializer = SpecialistCompeleteInfoSerializer(Specialists, many=True)
   return Response(serializer.data)

#Get This Specialists Primary Info
class GetThisSpecialistPrimaryInfo(APIView):
 def get(self, request, format='json'):
   if request.user.is_anonymous:
    return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
   if request.user.type == NewUser.Types.MEMBER:
    return Response("You're not a Specialist!", status=status.HTTP_401_UNAUTHORIZED)
   SpecialistToGet = request.user
   SpecialistInfo = Specialist.objects.get(id=SpecialistToGet.id)
   serializer = UserSerializer(SpecialistInfo)
   return Response(serializer.data)

#Get This Specialists Secondary Info
class GetThisSpecialistPrimaryInfo(APIView):
 def get(self, request, format='json'):
   if request.user.is_anonymous:
    return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
   if request.user.type == NewUser.Types.MEMBER:
    return Response("You're not a Specialist!", status=status.HTTP_401_UNAUTHORIZED)
   SpecialistToGet = request.user
   SpecialistInfo = SpecilistFields.objects.get(user=SpecialistToGet)
   serializer = SpecialistCompeleteInfoSerializer(SpecialistInfo)
   return Response(serializer.data)

#Get Specialists Secondary Info By Id
class GetSpecialistIdPrimaryInfo(APIView):
 def post(self, request, pk):
   if request.user.type == NewUser.Types.MEMBER:
    return Response("You Cant Get Info!", status=status.HTTP_401_UNAUTHORIZED)
   SpecialistToGet = NewUser.objects.get(id=pk)
   SpecialistInfo = SpecilistFields.objects.get(user=SpecialistToGet)
   serializer = SpecialistCompeleteInfoSerializer(SpecialistInfo)
   return Response(serializer.data)


#------- UPDATE
###############

#Create or Secondary Info
class UpdateSpecialistInfo(APIView):
    def post(self, request, format='json'):
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        if request.user.type == NewUser.Types.MEMBER:
            return Response("You're not a Specialist!", status=status.HTTP_401_UNAUTHORIZED)
        specialistfieldsobj, created = SpecilistFields.objects.get_or_create(user = request.user)
        serializer = SpecialistCompeleteInfoSerializer(data=request.data)
        if serializer.is_valid():
         specialistfieldsobj.id_code = serializer.data["id_code"]
         specialistfieldsobj.birth_date = serializer.data["birth_date"]
         specialistfieldsobj.degree = serializer.data["degree"]
         specialistfieldsobj.major = serializer.data["major"]
         specialistfieldsobj.phone_number = serializer.data["phone_number"]
         specialistfieldsobj.about = serializer.data["about"]
         specialistfieldsobj.address = serializer.data["address"]
         specialistfieldsobj.is_online = serializer.data["is_online"]
         specialistfieldsobj.rate = serializer.data["rate"]
         specialistfieldsobj.save()
         if specialistfieldsobj:
             return Response("Specialist Info has been updated!", status=status.HTTP_200_OK)
         return Response("OOOPS! Somthing went wrong!", status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#------- DELETE
###############
class RemoveSpecialist(APIView):
 def delete(self, request, format='json'):
  serializer = SpecialistIdSerializer(data=request.data)
  if serializer.is_valid():
   if request.user.type == NewUser.Types.MEMBER:
    return Response("You're not a Specialist!", status=status.HTTP_401_UNAUTHORIZED)
   UserToDelete = SpecilistFields.objects.get(user=serializer.data["id"])
   if NewUser.objects.filter(id=UserToDelete.id).exists() == False:
     return Response("This Specialist does NOT Exist!", status=status.HTTP_422_UNPROCESSABLE_ENTITY)
   try:
    Specialist.objects.filter(id=UserToDelete.id).delete()
    SpecilistFields.objects.filter(user=UserToDelete).delete()
   except ProtectedError:
    return Response("Can NOT Remove This Specialist", status=status.HTTP_400_BAD_REQUEST)
   return Response("Specialist removed from the cart.",  status=status.HTTP_200_OK)
  return Response("Data is Not Valid!", status=status.HTTP_400_BAD_REQUEST)