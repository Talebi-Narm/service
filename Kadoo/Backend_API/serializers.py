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

class paginatorSerializer(serializers.Serializer):
    count = serializers.IntegerField(required=True)
    page = serializers.IntegerField(required=True)

class sortSerializer(serializers.Serializer):
    kind = serializers.ChoiceField(required=True,
        choices = ['name', 'price', 'time']
    )
    order = serializers.ChoiceField(required=False, default='ASC',
        choices = ['ASC', 'DES']
    )

class nameSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    pagination = paginatorSerializer(required=False, default=None)
    sort = sortSerializer(required=False, default=None)
    
class priceSerializer(serializers.Serializer):
    lower = serializers.IntegerField(required=False, default=0)
    higher = serializers.IntegerField(required=False, default=inf)
    pagination = paginatorSerializer(required=False, default=None)
    sort = sortSerializer(required=False, default=None)
    
class environmentSerializer(serializers.Serializer):
    environment = serializers.ChoiceField(required=True,
        choices = ['cold', 'tropical', 'none']
    )
    pagination = paginatorSerializer(required=False, default=None)
    sort = sortSerializer(required=False, default=None)
    
class waterSerializer(serializers.Serializer):
    water = serializers.ChoiceField(required=True,
        choices = ['low', 'medium', 'much']
    )
    pagination = paginatorSerializer(required=False, default=None)
    sort = sortSerializer(required=False, default=None)
    
class lightSerializer(serializers.Serializer):
    light = serializers.ChoiceField(required=True,
        choices = ['low', 'medium', 'much']
    )
    pagination = paginatorSerializer(required=False, default=None)
    sort = sortSerializer(required=False, default=None)
class growthRateSerializer(serializers.Serializer):
    growthRate = serializers.ChoiceField(required=True,
        choices = ['low', 'medium', 'much']
    )
    pagination = paginatorSerializer(required=False, default=None)
    sort = sortSerializer(required=False, default=None)

class tagsSerializer(serializers.Serializer):
    tags = serializers.ListField(required=False, default=[],
        child = serializers.CharField(required=True)
    )

class plantAdvanceSerializer(serializers.Serializer):    
    name = serializers.CharField(required=False, default=None, allow_null=True,)
    price = priceSerializer(required=False, default=None, allow_null=True)
    environment = serializers.ChoiceField(required=False, default=None, allow_null=True,
        choices = ['cold', 'tropical', 'none']
    )
    water = serializers.ChoiceField(required=False, default=None, allow_null=True,
        choices = ['low', 'medium', 'much']
    )
    light = serializers.ChoiceField(required=False, default=None, allow_null=True,
        choices = ['low', 'medium', 'much']
    )
    growthRate = serializers.ChoiceField(required=False, default=None, allow_null=True,
        choices = ['low', 'medium', 'much']
    )
    tags = serializers.ListField(required=False, default=[], allow_null=True,
        child = serializers.CharField(required=True)
    )
    pagination = paginatorSerializer(required=False, default=None, allow_null=True)
    sort = sortSerializer(required=False, default=None, allow_null=True)

class toolAdvanceSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, default=None, allow_null=True)
    price = priceSerializer(required=False, default=None, allow_null=True,)
    tags = serializers.ListField(required=False, default=[], allow_null=True,
        child = serializers.CharField(required=True)
    )
    pagination = paginatorSerializer(required=False, default=None, allow_null=True)
    sort = sortSerializer(required=False, default=None, allow_null=True)