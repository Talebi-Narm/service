from rest_framework import serializers
from .models import myPlant

class myPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = myPlant
        fields = '__all__'

class addPlantSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=False, default = None)
    location = serializers.CharField(required=False, default=None)
    image = serializers.ImageField(required=False , default=None)

class updatePlantSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, default=None)
    description = serializers.CharField(required=False, default = None)
    location = serializers.CharField(required=False, default=None)
    image = serializers.ImageField(required=False , default=None)
