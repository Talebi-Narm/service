from rest_framework import serializers
from .models import Plant, Tool
from common.models import Tag

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'

class PlantSerializerCU(serializers.ModelSerializer):
    class Meta:
        model = Plant
        exclude = ['album', 'tags']

class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = '__all__'

class ToolSerializerCU(serializers.ModelSerializer):
    class Meta:
        model = Tool
        exclude = ['album', 'tags']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class paginatorSerializer(serializers.Serializer):
    count = serializers.IntegerField(required=True, allow_null=True)
    page = serializers.IntegerField(required=False, default=1, allow_null=True)

class sortSerializer(serializers.Serializer):
    kind = serializers.ChoiceField(required=True, allow_null=True,
        choices = ['name', 'price', 'time']
    )
    order = serializers.ChoiceField(required=False, default='ASC', allow_null=True,
        choices = ['ASC', 'DES']
    )

# class nameSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True)
#     pagination = paginatorSerializer(required=False, default=None)
#     sort = sortSerializer(required=False, default=None)

class priceSerializer(serializers.Serializer):
    lower = serializers.IntegerField(required=False, default=0, allow_null=True)
    higher = serializers.IntegerField(required=False, default=-1, allow_null=True)
    pagination = paginatorSerializer(required=False, default=None)
    sort = sortSerializer(required=False, default=None)

# class environmentSerializer(serializers.Serializer):
#     environment = serializers.ChoiceField(required=True, allow_null=True,
#         choices = ['cold', 'tropical', 'none']
#     )
#     pagination = paginatorSerializer(required=False, default=None)
#     sort = sortSerializer(required=False, default=None, allow_null=True)

# class waterSerializer(serializers.Serializer):
#     water = serializers.ChoiceField(required=True, allow_null=True,
#         choices = ['low', 'medium', 'much']
#     )
#     pagination = paginatorSerializer(required=False, default=None, allow_null=True)
#     sort = sortSerializer(required=False, default=None, allow_null=True)

# class lightSerializer(serializers.Serializer):
#     light = serializers.ChoiceField(required=True,allow_null=True,
#         choices = ['low', 'medium', 'much']
#     )
#     pagination = paginatorSerializer(required=False, default=None, allow_null=True)
#     sort = sortSerializer(required=False, default=None, allow_null=True)
# class growthRateSerializer(serializers.Serializer):
#     growthRate = serializers.ChoiceField(required=True,allow_null=True,
#         choices = ['low', 'medium', 'much']
#     )
#     pagination = paginatorSerializer(required=False, default=None, allow_null=True)
#     sort = sortSerializer(required=False, default=None, allow_null=True)

# class tagsSerializer(serializers.Serializer):
#     tags = serializers.ListField(required=False, default=[], allow_null=True,
#         child = serializers.CharField(required=True)
#     )

class plantAdvanceSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, default=None, allow_null=True)
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
    onlyAvailables = serializers.BooleanField(required=False, default=False, allow_null=True)
    pagination = paginatorSerializer(required=False, default=None, allow_null=True)
    sort = sortSerializer(required=False, default=None, allow_null=True)

class toolAdvanceSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, default=None, allow_null=True)
    price = priceSerializer(required=False, default=None, allow_null=True,)
    tags = serializers.ListField(required=False, default=[], allow_null=True,
        child = serializers.CharField(required=True)
    )
    onlyAvailables = serializers.BooleanField(required=False, default=False, allow_null=True)
    pagination = paginatorSerializer(required=False, default=None, allow_null=True)
    sort = sortSerializer(required=False, default=None, allow_null=True)

class allAdvanceSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, default=None, allow_null=True)
    price = priceSerializer(required=False, default=None, allow_null=True,)
    onlyAvailables = serializers.BooleanField(required=False, default=False, allow_null=True)
    pagination = paginatorSerializer(required=False, default=None, allow_null=True)
    sort = sortSerializer(required=False, default=None, allow_null=True)