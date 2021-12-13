from django.shortcuts import render
from django.db.models.deletion import ProtectedError
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from Coin.models import CoinManagementModel, LastSeenLogModel, LastWateringLogModel

import datetime

from .serializers import CoinSerializer, CoinValueSerializer, CoinValueWithIdSerializer
from Users.models import Member

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        '(post) Update Coin Value With New Value (*value)':'/upadte-value/',
        '(post) Update Coin Value With New Value For User With ID (*Id,*value)':'/update-value-Id/',
        '(post) Add New Value To Coin Value (*value)':'/add-value/',
        '(post) Add New Value To Coin Value For User With ID (*Id,*value)':'/add-value-Id/',
        '(post) Reduce New Value From Coin Value (*value)':'/reduce-value/',
        '(post) Reduce New Value From Coin Value For User With ID (*Id,*value)':'/reduce-value-Id/',
        '(get) All Coin Data':'/get-all/',
        '(get) This User Coin Data':'/get/',
        '(get) Coin Data Of User With Id':'/get/<str:pk>/',
        '######## Auto Update Coin':'',
        '(post) Daily Login Update':'/daily-login-update/',
        '(post) Daily Watering Update':'/daily-watering-update/',
        '(post) Weekly Login Update':'/weekly-login-update/',
        '(post) Weekly Watering Update':'/weekly-watering-update/',
        '######## Login Watering Log':'',
        '(post) New Login Record':'/new-login/',
        '(post) New Watering Record':'/new-watering/',
    }
    return Response(api_urls)


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
            UserToUpdate = Member.objects.get(id=serializer.data["id"])
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
            UserToUpdate = Member.objects.get(id=serializer.data["id"])
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
            UserToUpdate = Member.objects.get(id=serializer.data["id"])
            CoinData = CoinManagementModel.objects.get(user=UserToUpdate)
            CoinValue = serializer.data["value"]
            CoinData.coin_value -= CoinValue
            CoinData.save()
            if CoinData:
                return Response("Coin value updated successfully.", status=status.HTTP_200_OK)
            return Response("OOOPS! Something Went Wrong!", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#------- Auto Update
###############

#Auto Update Login Daily Coin This User
class DailyUpdateLoginUserCoin(APIView):
    def post(self, request):
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        UserToUpdate = request.user
        CoinData = CoinManagementModel.objects.get(user=UserToUpdate)
        TodayDate = datetime.date.today()
        YesterdayDate = datetime.date.today() - datetime.timedelta(days=1)
        print(TodayDate)
        print(YesterdayDate)
        CountLogInToday = LastSeenLogModel.objects.filter(date = TodayDate).count()
        CountLogInYesterday = LastSeenLogModel.objects.filter(date= YesterdayDate).count()
        print(CountLogInToday)
        print(CountLogInYesterday)
        if (CountLogInToday != 0 and CountLogInYesterday != 0):
            CoinValue = 5
            CoinData.coin_value += CoinValue
            CoinData.save()
            if CoinData:
                return Response("Keep Going! Your Doing Good!", status=status.HTTP_200_OK)
            return Response("OOOPS! Something Went Wrong!", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response("No Login for past two days.", status=status.HTTP_202_ACCEPTED)

#Auto Update Watering Daily Coin This User
class DailyUpdateWateringUserCoin(APIView):
    def post(self, request):
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        UserToUpdate = request.user
        CoinData = CoinManagementModel.objects.get(user=UserToUpdate)
        TodayDate = datetime.date.today()
        YesterdayDate = datetime.date.today() - datetime.timedelta(days=1)
        print(TodayDate)
        print(YesterdayDate)
        CountLogInToday = LastWateringLogModel.objects.filter(date = TodayDate).count()
        CountLogInYesterday = LastWateringLogModel.objects.filter(date = YesterdayDate).count()
        if (CountLogInToday == 1 and CountLogInYesterday != 0):
            CoinValue = 7
            CoinData.coin_value += CoinValue
            CoinData.save()
            if CoinData:
                return Response("Keep Going! Your Doing Good!", status=status.HTTP_200_OK)
            return Response("OOOPS! Something Went Wrong!", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response("No Login for past two days.", status=status.HTTP_202_ACCEPTED)

#Auto Update Login Weekly Coin This User
class WeeklyUpdateLoginUserCoin(APIView):
    def post(self, request):
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        UserToUpdate = request.user
        CoinData = CoinManagementModel.objects.get(user=UserToUpdate)
        flag = True
        for i in range(6):
            DateToCheck = datetime.date.today() - datetime.timedelta(days=i)
            CountLogIn = LastSeenLogModel.objects.filter(date = DateToCheck).count()
            if (CountLogIn == 0):
                flag = False
                break
        if flag == True:
            CoinValue = 25
            CoinData.coin_value += CoinValue
            CoinData.save()
            if CoinData:
                return Response("Keep Going! Your Doing Good!", status=status.HTTP_200_OK)
            return Response("OOOPS! Something Went Wrong!", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response("No Login for past week.", status=status.HTTP_202_ACCEPTED)

#Auto Update Watering Weekly Coin This User
class WeeklyUpdateWateringUserCoin(APIView):
    def post(self, request):
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        UserToUpdate = request.user
        CoinData = CoinManagementModel.objects.get(user=UserToUpdate)
        flag = True
        for i in range(6):
            DateToCheck = datetime.date.today() - datetime.timedelta(days=i)
            CountLogIn = LastWateringLogModel.objects.filter(date = DateToCheck).count()
            if (CountLogIn == 0):
                flag = False
                break
        if flag == True:
            CoinValue = 50
            CoinData.coin_value += CoinValue
            CoinData.save()
            if CoinData:
                return Response("Keep Going! Your Doing Good!", status=status.HTTP_200_OK)
            return Response("OOOPS! Something Went Wrong!", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response("No Login for past week.", status=status.HTTP_202_ACCEPTED)


#------- Read
###############

#Read All Coin Data
class GetTAllCoin(APIView):
    def get(self, request, format='json'):
        CoinInfo = CoinManagementModel.objects.all()
        serializer = CoinSerializer(CoinInfo, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#Read Coin Data For This User
class GetThisUserCoin(APIView):
    def get(self, request, format='json'):
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        UserToGet = request.user
        if CoinManagementModel.objects.filter(user = UserToGet).exists() == False:
            return Response("There is No Data for this User", status=status.HTTP_404_NOT_FOUND)
        CoinInfo = CoinManagementModel.objects.get(user = UserToGet)
        print(CoinInfo)
        serializer = CoinSerializer(CoinInfo)
        return Response(serializer.data, status=status.HTTP_200_OK)

#Read Coin Data With ID
class GetUserCoinWithId(APIView):
    def get(self, request, pk, format='json'):
        if Member.objects.filter(id=pk).exists() == False:
            return Response("This User Does NOT exist!", status=status.HTTP_404_NOT_FOUND)
        UserToGet = Member.objects.get(id=pk)
        CoinInfo = CoinManagementModel.objects.get(user = UserToGet)
        serializer = CoinSerializer(CoinInfo)
        return Response(serializer.data, status=status.HTTP_200_OK)



#######################
#------------ Login Watering
#######################

#New Login Record
class AddLogin(APIView):
 def post(self, request):
    if request.user.is_anonymous:
      return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
    userToAdd = request.user
    LoginLog = LastSeenLogModel.objects.create(user=userToAdd)
    LoginLog.save()
    if LoginLog:
      return Response("Login Log Created.", status=status.HTTP_201_CREATED)
    return Response("OOOPS! Something went wrong!", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Addwatering(APIView):
 def post(self, request):
    if request.user.is_anonymous:
      return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
    userToAdd = request.user
    LoginLog = LastWateringLogModel.objects.create(user=userToAdd)
    LoginLog.save()
    if LoginLog:
      return Response("Login Log Created.", status=status.HTTP_201_CREATED)
    return Response("OOOPS! Something went wrong!", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


