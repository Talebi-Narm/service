import json

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Ticket


@receiver(post_save, sender=Ticket, dispatch_uid="notify_new_ticket")
def notify_new_ticket(sender, instance, created, **kwargs):
    channel_layer = get_channel_layer()
    queryset = Ticket.objects.filter(is_closed=False, specialist=None)
    data = list(queryset.values())
    serialized_data = json.dumps(data, cls=DjangoJSONEncoder)  # remove UUID error
    data = json.loads(serialized_data)

    async_to_sync(channel_layer.group_send)("specialists", {
        'type': 'system_message',
        'message': data
    })
