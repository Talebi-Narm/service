from rest_framework import serializers
from .models import myPlant

class myPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = myPlant
        fields = '__all__'

class addPlantSerializer(serializers.Serializer):
    plant = serializers.CharField(required=True)
    location = serializers.CharField(required=False, default=None)
    image = serializers.ImageField(required=False , default=None)
