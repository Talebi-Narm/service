from django.db.models.enums import Choices
from rest_framework import serializers
from Backend.models import Plant
from Specialist.models import SpecialistFieldsManager
from Users.models import Member, MemberFields, NewUser
from rest_framework.validators import UniqueValidator


class CustomMemberSerializer(serializers.ModelSerializer):
    
    type = serializers.CharField(required=False, default=NewUser.Types.MEMBER)
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=NewUser.objects.all(), message="This Email is Already Taken!")])
    user_name = serializers.CharField(required=True, validators=[UniqueValidator(queryset=NewUser.objects.all(), message="This Username is Already Taken!")])
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
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('id','type','email', 'user_name', 'first_name', 'last_name')