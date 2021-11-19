from django.shortcuts import render
from django.db.models.deletion import ProtectedError
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from Coin.models import CoinManagementModel

from serializers import CoinSerializer, CoinValueSerializer, CoinValueWithIdSerializer
from Users.models import Member

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        '(post) Update Coin Value With New Value (*value)':'/upadte-value/',
        '(post) Update Coin Value With New Value For User With ID (*Id,*value)':'/update-value/<str:pk>/',
        '(post) Add New Value To Coin Value (*value)':'/add-value/',
        '(post) Add New Value To Coin Value For User With ID (*Id,*value)':'/add-value-Id/',
        '(post) Reduce New Value From Coin Value (*value)':'/reduce-value/',
        '(post) Reduce New Value From Coin Value For User With ID (*Id,*value)':'/reduce-value-Id/',
        '(get) All Coin Data':'/get-all/',
        '(get) This User Coin Data':'/get/',
        '(get) Coin Data Of User With Id':'/get/<str:pk>/',
    }
    return response.Response(api_urls)


#######################
#------------ CRUD Coin
#######################

#------- Update
###############

#Update This User Coin Value
class UpdateThisUserCoin(APIView):
    def post(self, request, format='json'):
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        UserToUpdate = request.user
        serializer = CoinValueSerializer(data=request.data)
        
        if serializer.is_valid():
            CoinData = CoinManagementModel.objects.get(user=UserToUpdate)
            CoinValue = serializer.data["value"]
            CoinData.coin_value = CoinValue
            CoinData.save()
            if CoinData:
                return Response("Coin value updated successfully.", status=status.HTTP_200_OK)
            return Response("OOOPS! Something Went Wrong!", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Update User Coin Value With ID
class UpdateUserCoinWithId(APIView):
    def post(self, request, format='json'):
        serializer = CoinValueWithIdSerializer(data=request.data)
        if serializer.is_valid():
            if Member.objects.filter(id=serializer.data["id"]).exists() == False:
                return Response("This User Does NOT exist!", status=status.HTTP_404_NOT_FOUND)
            UserToGet = Member.objects.get(id=serializer.data["id"])
            CoinData = CoinManagementModel.objects.get(user=UserToUpdate)
            CoinValue = serializer.data["value"]
            CoinData.coin_value = CoinValue
            CoinData.save()
            if CoinData:
                return Response("Coin value updated successfully.", status=status.HTTP_200_OK)
            return Response("OOOPS! Something Went Wrong!", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Add This User Coin Value
class AddThisUserCoin(APIView):
    def post(self, request, format='json'):
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        UserToUpdate = request.user
        serializer = CoinValueSerializer(data=request.data)
        
        if serializer.is_valid():
            CoinData = CoinManagementModel.objects.get(user=UserToUpdate)
            CoinValue = serializer.data["value"]
            CoinData.coin_value += CoinValue
            CoinData.save()
            if CoinData:
                return Response("Coin value updated successfully.", status=status.HTTP_200_OK)
            return Response("OOOPS! Something Went Wrong!", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Add User Coin Value With ID
class AddUserCoinWithId(APIView):
    def post(self, request, format='json'):
        serializer = CoinValueWithIdSerializer(data=request.data)
        if serializer.is_valid():
            if Member.objects.filter(id=serializer.data["id"]).exists() == False:
                return Response("This User Does NOT exist!", status=status.HTTP_404_NOT_FOUND)
            UserToGet = Member.objects.get(id=serializer.data["id"])
            CoinData = CoinManagementModel.objects.get(user=UserToUpdate)
            CoinValue = serializer.data["value"]
            CoinData.coin_value += CoinValue
            CoinData.save()
            if CoinData:
                return Response("Coin value updated successfully.", status=status.HTTP_200_OK)
            return Response("OOOPS! Something Went Wrong!", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Reduce This User Coin Value
class ReduceThisUserCoin(APIView):
    def post(self, request, format='json'):
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        UserToUpdate = request.user
        serializer = CoinValueSerializer(data=request.data)
        
        if serializer.is_valid():
            CoinData = CoinManagementModel.objects.get(user=UserToUpdate)
            CoinValue = serializer.data["value"]
            CoinData.coin_value -= CoinValue
            CoinData.save()
            if CoinData:
                return Response("Coin value updated successfully.", status=status.HTTP_200_OK)
            return Response("OOOPS! Something Went Wrong!", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Reduce User Coin Value With ID
class ReduceUserCoinWithId(APIView):
    def post(self, request, format='json'):
        serializer = CoinValueWithIdSerializer(data=request.data)
        if serializer.is_valid():
            if Member.objects.filter(id=serializer.data["id"]).exists() == False:
                return Response("This User Does NOT exist!", status=status.HTTP_404_NOT_FOUND)
            UserToGet = Member.objects.get(id=serializer.data["id"])
            CoinData = CoinManagementModel.objects.get(user=UserToUpdate)
            CoinValue = serializer.data["value"]
            CoinData.coin_value -= CoinValue
            CoinData.save()
            if CoinData:
                return Response("Coin value updated successfully.", status=status.HTTP_200_OK)
            return Response("OOOPS! Something Went Wrong!", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#------- Read
###############

#Read All Coin Data
class GetTAllCoin(APIView):
    def get(self, request, format='json'):
        CoinInfo = CoinManagementModel.objects.all
        serializer = CoinSerializer(CoinInfo, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#Read Coin Data For This User
class GetThisUserCoin(APIView):
    def get(self, request, format='json'):
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        UserToGet = request.user
        CoinInfo = CoinManagementModel.objects.filter(user = UserToGet)
        serializer = CoinSerializer(CoinInfo)
        return Response(serializer.data, status=status.HTTP_200_OK)

#Read Coin Data With ID
class GetUserCoinWithId(APIView):
    def get(self, request, pk, format='json'):
        if Member.objects.filter(id=pk).exists() == False:
            return Response("This User Does NOT exist!", status=status.HTTP_404_NOT_FOUND)
        UserToGet = Member.objects.get(id=pk)
        CoinInfo = CoinManagementModel.objects.filter(user = UserToGet)
        serializer = CoinSerializer(CoinInfo)
        return Response(serializer.data, status=status.HTTP_200_OK)

