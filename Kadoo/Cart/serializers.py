from rest_framework import serializers

from Cart.models import PlantCartModel

class CartPlantSerializer(serializers.Serializer):
 id = serializers.UUIDField(required=True)
 count = serializers.IntegerField(required=False, default = 1)
 description = serializers.CharField(required=False, default = "null")

 