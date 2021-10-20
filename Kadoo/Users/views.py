from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import CustomMemberSerializer
from rest_framework_simplejwt.tokens import RefreshToken

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
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    