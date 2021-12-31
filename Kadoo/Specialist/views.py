from django.db.models.deletion import ProtectedError
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from Specialist.models import Specialist, SpecilistFields
from django.contrib.auth.models import Group

from Specialist.serializers import CustomSpecialistSerializer, SpecialistCompeleteInfoSerializer, SpecialistCompeleteInfoSerializerPost, SpecialistIdSerializer
from Users.models import NewUser
from Users.serializers import UserSerializer


@api_view(['GET'])
def apiOverview(request):
    """See All Specialist API"""
    api_urls = {
        '(post) Register A User (*email,*username,*firstname,*lastname,*password)':'/register/',
        '(get) Get All Specialists Primary Info':'/all-primary/',
        '(get) Get All Specialists Secondary Info':'/all-secondary/',
        '(get) Get This Specialist Primary Info':'/primary/',
        '(get) Get This Specialist Secondary Info':'/secondary/',
        '(get) Get Specialist Secondary Info By Id':'/secondary/<str:pk>/',
        '(get) Get Specialist Primary Info By Id':'/primary/<str:pk>/',
        '(post) Update A Specialist Secondary Info By Id (id_code, birth_date, degree, major, phone_number, about,address,is_online, rate)':'/update-secondary/<str:pk>/',
        '(post) Update A Specialist Primary Info(*id,*email,*username,*firstname,*lastname,*password)':'/update-primary/',
        '(delete) Delete Specialist By Id (*id)':'/delete/',
    }
    return Response(api_urls)


#######################
#------------ CRUD Specialist
#######################


#------- CREATE
###############

#Create Specialists
class CustomSpecialistCreate(generics.GenericAPIView):
    serializer_class = CustomSpecialistSerializer
    permission_classes = [AllowAny]
    def post(self, request, format='json'):
        """Register A User (*email,*username,*firstname,*lastname,*password)"""
        serializer = CustomSpecialistSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                Specialist_group = Group.objects.get(name='SpecialistGroup') 
                Specialist_group.user_set.add(user)
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#------- READ
###############

#Get All Specialists Primary Info
class GetAllSpecialistPrimaryInfo(APIView):
 serializer_class = UserSerializer
 def get(self, request, format='json'):
   """Get All Specialists Primary Info"""
   Specialists = Specialist.objects.filter(type=NewUser.Types.SPECIALIST)
   serializer = UserSerializer(Specialists, many=True)
   return Response(serializer.data)

#Get All Specialists Secondary Info
class GetAllSpecialistSecondaryInfo(APIView):
 serializer_class = SpecialistCompeleteInfoSerializer
 def get(self, request, format='json'):
   """Get All Specialists Secondary Info"""
   Specialists = SpecilistFields.objects.all()
   serializer = SpecialistCompeleteInfoSerializer(Specialists, many=True)
   return Response(serializer.data)

#Get This Specialists Primary Info
class GetThisSpecialistPrimaryInfo(APIView):
 serializer_class = UserSerializer
 def get(self, request, format='json'):
   """Get This Specialist Primary Info"""
   if request.user.is_anonymous:
    return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
   if request.user.type == NewUser.Types.MEMBER:
    return Response("You're not a Specialist!", status=status.HTTP_401_UNAUTHORIZED)
   SpecialistToGet = request.user
   SpecialistInfo = Specialist.objects.get(id=SpecialistToGet.id)
   serializer = UserSerializer(SpecialistInfo)
   return Response(serializer.data)

#Get This Specialists Secondary Info
class GetThisSpecialistSecondaryInfo(APIView):
 serializer_class = SpecialistCompeleteInfoSerializer
 def get(self, request, format='json'):
   """Get This Specialist Secondary Info"""
   if request.user.is_anonymous:
    return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
   if request.user.type == NewUser.Types.MEMBER:
    return Response("You're not a Specialist!", status=status.HTTP_401_UNAUTHORIZED)
   SpecialistToGet = request.user
   if SpecilistFields.objects.filter(user = SpecialistToGet).exists() == False:
    return Response("No Info Set For This Specialist!", status=status.HTTP_404_NOTFOUND)
   SpecialistInfo = SpecilistFields.objects.get(user=SpecialistToGet)
   serializer = SpecialistCompeleteInfoSerializer(SpecialistInfo)
   return Response(serializer.data)

#Get Specialists Secondary Info By Id
class GetSpecialistIdSecondaryInfo(APIView):
 def get(self, request, pk):
   """Get Specialist Secondary Info By Id"""
   if request.user.type == NewUser.Types.MEMBER:
    return Response("You Cant Get Info!", status=status.HTTP_401_UNAUTHORIZED)
   SpecialistToGet = NewUser.objects.get(id=pk)
   if SpecilistFields.objects.filter(user = SpecialistToGet).exists() == False:
    return Response("No Info Set For This Specialist!", status=status.HTTP_404_NOT_FOUND)
   SpecialistInfo = SpecilistFields.objects.get(user=SpecialistToGet)
   serializer = SpecialistCompeleteInfoSerializer(SpecialistInfo)
   return Response(serializer.data)

#Get Specialists Primary Info By Id
class GetSpecialistIdPrimaryInfo(APIView):
 def get(self, request, pk, format='json'):
   """Get This Specialist Primary Info"""
   if request.user.type == NewUser.Types.MEMBER:
    return Response("You Cant Get Info!", status=status.HTTP_401_UNAUTHORIZED)
   SpecialistToGet = NewUser.objects.get(id=pk)
   serializer = UserSerializer(SpecialistToGet)
   return Response(serializer.data)

#------- UPDATE
###############

#Update Secondary Info
class UpdateSpecialistInfo(generics.GenericAPIView):
    serializer_class = SpecialistCompeleteInfoSerializerPost
    def post(self, request, pk, format='json'):
        """Update this User Secondary Info (id_code, birth_date, degree, major, phone_number, about,address,is_online, rate)"""
        #if request.user.is_anonymous:
            #return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        #if request.user.type == NewUser.Types.MEMBER:
            #return Response("You're not allowed!", status=status.HTTP_401_UNAUTHORIZED)
        SpecialistToGet = NewUser.objects.get(id=pk)
        specialistfieldsobj, created = SpecilistFields.objects.get_or_create(user = SpecialistToGet)
        serializer = SpecialistCompeleteInfoSerializerPost(data=request.data)
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


#Update Primary Info
class UpdatePrimarySpecialistInfo(generics.GenericAPIView):
    serializer_class = UserSerializer
    def post(self, request,pk, format='json'):
        """Update this User Primary Info"""
        #if request.user.is_anonymous:
            #return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        #if request.user.type != NewUser.Types.ADMIN:
           # return Response("You're not a Specialist!", status=status.HTTP_401_UNAUTHORIZED)
        #if NewUser.objects.filter(id=pk).exists() == False:
            #return Response("No Specialist With This Data!", status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
         SpecialistToGet = NewUser.objects.get(id=pk)
         SpecialistToGet.email = serializer.data["email"]
         SpecialistToGet.user_name = serializer.data["user_name"]
         SpecialistToGet.first_name = serializer.data["first_name"]
         SpecialistToGet.last_name = serializer.data["last_name"]
         SpecialistToGet.save()
         if SpecialistToGet:
             return Response("Specialist Info has been updated!", status=status.HTTP_200_OK)
         return Response("OOOPS! Somthing went wrong!", status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#------- DELETE
###############
class RemoveSpecialist(generics.GenericAPIView):
 serializer_class = SpecialistIdSerializer
 def delete(self, request, format='json'):
  """Delete Specialist By Id (*id)"""
  serializer = SpecialistIdSerializer(data=request.data)
  if serializer.is_valid():
   if request.user.type == NewUser.Types.MEMBER:
    return Response("You're not a Specialist!", status=status.HTTP_401_UNAUTHORIZED)
   UserToDelete = serializer.data["id"]
   if NewUser.objects.filter(id=UserToDelete).exists() == False:
     return Response("This Specialist does NOT Exist!", status=status.HTTP_422_UNPROCESSABLE_ENTITY)
   try:
    Specialist.objects.filter(id=UserToDelete).delete()
   except ProtectedError:
    return Response("Can NOT Remove This Specialist", status=status.HTTP_400_BAD_REQUEST)
   return Response("Specialist removed.",  status=status.HTTP_200_OK)
  return Response("Data is Not Valid!", status=status.HTTP_400_BAD_REQUEST)