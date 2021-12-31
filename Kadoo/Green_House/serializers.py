from rest_framework import serializers
from .models import myPlant

class myPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = myPlant
        fields = '__all__'