from rest_framework.serializers import ModelSerializer

from user.models import UserAddress


class UserAddressSerializer(ModelSerializer):
    class Meta:
        model = UserAddress
        exclude = ('is_deleted', 'deleted_at')
        read_only_fields = ('id', 'user')
