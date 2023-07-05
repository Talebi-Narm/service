from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from user.models import User, UserAddress
from user.serializers.user import UserProfileSerializer, AvatarSerializer, UserProfileUpdateSerializer


class UserProfile(GenericAPIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        responses={200: UserProfileSerializer}
    )
    def get(self, request):
        pk = request.user.id
        user = get_object_or_404(User, id=pk)
        addresses = UserAddress.objects.filter(owner=pk)
        user_addresses = [(address.id, address.address) for address in addresses]
        result = dict()
        result['user'] = user
        result['addresses'] = user_addresses
        result['avatar_url'] = user.avatar_url
        serializer = UserProfileSerializer(result, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=UserProfileUpdateSerializer,
    )
    def put(self, request):
        user = User.objects.filter(id=request.user.id).update(**request.data)
        return Response(status=status.HTTP_200_OK)


# API for updating user avatar
class UserAvatar(GenericAPIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    @extend_schema(
        request=AvatarSerializer,
        responses={200: AvatarSerializer}
    )
    def put(self, request):
        pk = request.user.id
        user = get_object_or_404(User, id=pk)
        serializer = AvatarSerializer(user, data=request.data)
        if serializer.is_valid():
            print(request.data['avatar_url'])
            user.avatar_url = request.data.get('avatar_url')
            user.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
