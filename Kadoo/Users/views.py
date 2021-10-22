from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from Backend.models import Plant
from Backend_API.serializers import PlantSerializer
from Users.models import MemberFields
from .serializers import CustomMemberSerializer, IdPlantSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view


class CurrentUserView(APIView):
    def get(self, request):
        if request.user.is_anonymous:
            return Response("AnonymousUser", status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class BlacklistUpdate(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class CustomMemberCreate(APIView):
    permission_classes = [AllowAny]
    def post(self, request, format='json'):
        serializer = CustomMemberSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            id = serializer.data('id')
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateCredit(APIView):
    @csrf_exempt
    def post(self, request,amount):
        memberfieldsobj, created = MemberFields.objects.get_or_create(user = request.user)
        PlantSerializer
        memberfieldsobj.credit_value = amount
        memberfieldsobj.save()
        if memberfieldsobj:
            return Response("Added", status=status.HTTP_201_CREATED)
        return Response("error", status=status.HTTP_400_BAD_REQUEST)
    

class AddPlantToCart(APIView):
    @csrf_exempt
    def post(self, request, format='json'):
        serializer = IdPlantSerializer(data=request.data)
        if serializer.is_valid():
            plant = Plant.objects.get(name=serializer.data["name"])
            memberfieldsobj, created = MemberFields.objects.get_or_create(user = request.user)
            memberfieldsobj.plants_cart.add(plant)
            memberfieldsobj.save()
            if memberfieldsobj:
                json = serializer.data
            return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

