from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from user.models import User, UserAddress
from user.serializers.user import UserProfileSerializer

class UserProfile(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        pk = request.user.id
        user = get_object_or_404(User, id=pk)
        addresses = UserAddress.objects.filter(owner=pk)
        user_addresses = [address['address'] for address in addresses]
        result = dict()
        result['user'] = user
        result['addresses'] = user_addresses
        serializer = UserProfileSerializer(result, many=False)
        return Response(serializer.data)
