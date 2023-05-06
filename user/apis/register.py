from rest_framework import generics

from user.models import User, Seller
from user.serializers.seller import SellerSerializer
from user.serializers.user import UserSerializer


class RegisterUserAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class RegisterSeller(generics.CreateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
