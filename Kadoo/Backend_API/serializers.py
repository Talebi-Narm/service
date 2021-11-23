from rest_framework import serializers
from Backend.models import Plant, Tool, Tag, Image, Album
from math import inf
class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'

class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class nameSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    
class priceSerializer(serializers.Serializer):
    lower = serializers.IntegerField(required=False, default=0)
    higher = serializers.IntegerField(required=False, default=inf)
    
class environmentSerializer(serializers.Serializer):
    environment = serializers.ChoiceField(required=True,
        choices = ['cold', 'tropical', 'none']
    )
    
class waterSerializer(serializers.Serializer):
    water = serializers.ChoiceField(required=True,
        choices = ['low', 'medium', 'much']
    )
    
class lightSerializer(serializers.Serializer):
    light = serializers.ChoiceField(required=True,
        choices = ['low', 'medium', 'much']
    )
class growthRateSerializer(serializers.Serializer):
    growthRate = serializers.ChoiceField(required=True,
        choices = ['low', 'medium', 'much']
    )

class plantAdvanceSerializer(serializers.Serializer):
    name = nameSerializer(required=False, default=None)
    price = priceSerializer(required=False, default=None)
    environment = environmentSerializer(required=False, default=None)
    water = waterSerializer(required=False, default=None)
    light = lightSerializer(required=False, default=None)
    growthRate = growthRateSerializer(required=False, default=None)
    tags = serializers.ListField(required=False, default=[],
        child = serializers.CharField(required=True)
    )

class toolAdvanceSerializer(serializers.Serializer):
    name = nameSerializer(required=False, default=None)
    price = priceSerializer(required=False, default=None)
    tags = serializers.ListField(required=False, default=[],
        child = serializers.CharField(required=True)
    )