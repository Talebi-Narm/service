from rest_framework import serializers

from Specialist.models import Specialist, SpecilistFields
from Users.models import NewUser
from rest_framework.validators import UniqueValidator

class CustomSpecialistSerializer(serializers.ModelSerializer):
    
    type = serializers.CharField(required=False, default=NewUser.Types.SPECIALIST)
    is_staff = serializers.BooleanField(required=False, default=True)
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=NewUser.objects.all(), message="This Email is Already Taken!")])
    user_name = serializers.CharField(required=True, validators=[UniqueValidator(queryset=NewUser.objects.all(), message="This Username is Already Taken!")])
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = Specialist
        fields = ('type','is_staff' ,'email', 'user_name', 'first_name', 'last_name', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
            'type': {'Read_only': True},
            'is_staff': {'Read_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance



class SpecialistCompeleteInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecilistFields
        fields = '__all__'

class SpecialistCompeleteInfoSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = SpecilistFields
        fields = ('id_code', 'birth_date', 'degree', 'major', 'phone_number', 'about','address','is_online', 'rate')


class SpecialistIdSerializer(serializers.Serializer):
 id = serializers.IntegerField(required=True)