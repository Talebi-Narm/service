from django.db.models.enums import Choices
from rest_framework import serializers
from Users.models import Member, NewUser


class CustomMemberSerializer(serializers.ModelSerializer):
    
    type = serializers.CharField(required=False, default=NewUser.Types.MEMBER)
    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = Member
        fields = ('type','email', 'user_name', 'first_name', 'last_name', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
            'type': {'Read_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        type = NewUser.Types.ADMIN
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance