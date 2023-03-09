from rest_framework import serializers
from core.models import Plant, Tool

from Cart.models import PlantCartModel, ToolCartModel

class CartItemSerializer(serializers.Serializer):
 id = serializers.UUIDField(required=True)
 count = serializers.IntegerField(required=False, default = 1)
 description = serializers.CharField(required=False, default = "null")

class CartItemIdSerializer(serializers.Serializer):
 id = serializers.UUIDField(required=True)

class DesicriptionSerializer(serializers.Serializer):
 description = serializers.CharField(required=False, default = "null")

class PlantCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantCartModel
        fields = '__all__'
        

class PlantWithCountCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'


class ToolCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolCartModel
        fields = '__all__'

class ToolWithCountCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = '__all__'