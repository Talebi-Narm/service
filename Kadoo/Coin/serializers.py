from rest_framework import serializers
from Coin.models import CoinManagementModel

class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinManagementModel
        fields = '__all__'

class CoinValueSerializer(serializers.Serializer):
    value = serializers.IntegerField(required=True)

class CoinValueWithIdSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=True)
    value = serializers.IntegerField(required=True)