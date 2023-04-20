from rest_framework.serializers import ModelSerializer

from user.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = (
            'is_staff', 'is_superuser', 'groups', 'user_permissions', 'created_at', 'deleted_at', 'updated_at', 'is_deleted',
            'is_active', 'calendar_id', 'calendar_token', 'phone_number')
        read_only_fields = ('id', 'last_login', 'date_joined', 'wallet_charge')
        extra_kwargs = {
            'password': {'write_only': True},
        }
