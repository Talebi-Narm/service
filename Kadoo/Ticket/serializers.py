from rest_framework import serializers
from Ticket.models import TicketModel

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketModel
        fields = '__all__'

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketModel
        fields = '__all__'

class RateSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=True)
    rate = serializers.IntegerField(required=True)
1
