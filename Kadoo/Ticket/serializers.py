from django.contrib.auth.models import User
from rest_framework import serializers
from Ticket.models import TicketModel, SupportTicketModel, ConversationModel
from Users.models import NewUser

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketModel
        fields = '__all__'

class CreateSupportTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportTicketModel
        fields = ('body','Category')

class GetSupportTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportTicketModel
        fields = ['id','ticket_author', 'ticket_specialist', 'ticket_status', 'Category', 'body', 'created', 'modified']

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConversationModel
        fields = '__all__'


class RateSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=True)
    rate = serializers.IntegerField(required=True)
1
