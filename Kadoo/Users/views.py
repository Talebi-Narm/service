from rest_framework import status
from rest_framework import response
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from Users.models import MemberFields
from .serializers import CustomMemberSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from rest_framework import generics

@api_view(['GET'])
def apiOverview(request):
    """See All User API"""
    api_urls = {
        '(post) Register A User (*email,*username,*firstname,*lastname,*password)':'/register/',
        '(post) Login (get tokens)  (*email,*password)':'/token/',
        '(post) Get Token with Refresh':'/token/refresh/',
        '(post) logout':'/logout/',
        '(get) Get Logedin User Information':'/userinfo/',
        '(post) Update Credit of User':'/updatecredit/<int:amount>/',
    }
    return response.Response(api_urls)

class CurrentUserView(APIView):
    #GET CURRENT USER
    #HTTP_401 : No Login
    """Get Logedin User Information"""
    serializer_class = UserSerializer
    def get(self, request):
        if request.user.is_anonymous:
            return Response("Anonymous User: You should login first.", status=status.HTTP_401_UNAUTHORIZED)
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class BlacklistUpdate(APIView):
    #USER LOGIUT (PUT TOKEN TO BLACK LIST)
    #HTTP_400 : Bad request caused by wrong token
    """Logout"""
    permission_classes = [AllowAny]
    authentication_classes = ()
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response("You've just logged out!", status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response("Somthing went wrong! Token is Not Valid! You may not have login yet.", status=status.HTTP_400_BAD_REQUEST)

class CustomMemberCreate(generics.GenericAPIView):
    """Register A User (*email,*username,*firstname,*lastname,*password)"""
    serializer_class = CustomMemberSerializer
    permission_classes = [AllowAny]
    def post(self, request, format='json'):
        serializer = CustomMemberSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateCredit(APIView):
    """Update Credit Of User"""
    @csrf_exempt
    #UPDATE CREDIT
    #HTTP_401 : No Login
    #HTTP_422 : Invalid value for credit (value >= 0)
    def post(self, request,amount):
        if request.user.is_anonymous:
            return Response("Anonymous User: You should first login.", status=status.HTTP_401_UNAUTHORIZED)
        memberfieldsobj, created = MemberFields.objects.get_or_create(user = request.user)
        if amount < 0:
            return Response("Credit value can NOT set less than zero!", status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        memberfieldsobj.credit_value = amount
        memberfieldsobj.save()
        if memberfieldsobj:
            return Response("Credit Valus has been updated to = " + str(amount) + " T", status=status.HTTP_200_OK)
        return Response("OOOPS! Somthing went wrong!", status=status.HTTP_400_BAD_REQUEST)
    

