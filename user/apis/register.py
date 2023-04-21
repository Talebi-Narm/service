from rest_framework import generics

from user.models import User
from user.serializers.user import UserSerializer


class RegisterUserAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
