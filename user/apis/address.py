from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from common.permissions.user import IsObjectOwner
from user.models import UserAddress
from user.serializers.address import UserAddressSerializer


class UserAddressList(ListCreateAPIView):
    swagger_tags = ('user address',)
    serializer_class = UserAddressSerializer
    queryset = UserAddress.objects.all()
    permission_classes = (IsAuthenticated, IsObjectOwner)


class UserAddressDetail(RetrieveUpdateDestroyAPIView):
    swagger_tags = ('user address',)
    serializer_class = UserAddressSerializer
    queryset = UserAddress.objects.all()
    permission_classes = (IsAuthenticated, IsObjectOwner)
