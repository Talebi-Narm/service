from rest_framework import serializers

from user.models import User, Gender


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            'is_staff', 'is_superuser', 'groups', 'user_permissions', 'created_at', 'deleted_at', 'updated_at',
            'is_deleted', 'is_active', 'calendar_id', 'calendar_token', 'phone_number')
        read_only_fields = ('id', 'last_login', 'date_joined', 'wallet_charge')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserProfileSerializer(serializers.Serializer):
    user = UserSerializer()
    addresses = serializers.ListField(
        child=serializers.CharField(max_length=250)
    )


class UserProfileUpdateSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone_number = serializers.CharField()
    email = serializers.EmailField()
    gender = serializers.ChoiceField(choices=Gender.choices, help_text=Gender.choices)
    about = serializers.CharField()


class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class AvatarSerializer(serializers.Serializer):
    avatar_url = serializers.ImageField()
