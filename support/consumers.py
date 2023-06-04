import json

from channels.db import database_sync_to_async
from channels.exceptions import DenyConnection
from channels.generic.websocket import AsyncJsonWebsocketConsumer, AsyncWebsocketConsumer
from django.db.models import Q

from .models import Ticket, Specialist


class ChatConsumer(AsyncJsonWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.room_name = None
        self.room_group_name = None
        self.is_specialist = None
        self.user = None

    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        self.user = self.scope['user']
        self.is_specialist = await database_sync_to_async(Specialist.objects.filter(user=self.user).exists)()

        if self.is_specialist:
            await self.connect_specialist()
        else:
            await self.connect_user()

    async def connect_user(self):
        # Check integrity of room name and token
        if str(self.user.pk) != self.room_name:
            error_message = "You are not authorized to join this room!"
            raise DenyConnection(error_message)

        # Join room group
        # self.channel_name is the unique channel name that the connection is identified by
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

        # Because it's new connection, we send a system message to the user not to the group
        await self.send_json({
            "type": "system_message",
            "message": "You have successfully connected to the room as a user!"
        })

    async def connect_specialist(self):
        await self.accept()
        if not await database_sync_to_async(Ticket.objects.filter(user__pk=self.room_name, is_closed=False).exists)():
            error_message = "This user does not have an open ticket!"
            await self.send_json({
                "type": "system_message",
                "error": error_message
            })
            await self.close()
            return
        elif await database_sync_to_async(
                Ticket.objects.filter(
                    ~Q(specialist__user=self.user),
                    user__pk=self.room_name,
                    is_closed=False,
                    specialist__isnull=False
                ).exists)():
            error_message = "This user already has a specialist!"
            await self.send_json({
                "type": "system_message",
                "error": error_message
            })
            await self.close()
            return
        else:
            # Join room group
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
            specialist = await database_sync_to_async(Specialist.objects.get)(user=self.user)
            await database_sync_to_async(
                Ticket.objects.filter(
                    user__pk=self.room_name,
                    is_closed=False,
                    specialist__isnull=True
                ).update)(specialist=specialist)

            # Because it's new connection, we send a system message to the user not to the group
            await self.send_json({
                "type": "system_message",
                "message": "You have successfully connected to the room as a specialist!"
            })

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def get_key(self, content, key):
        if key not in content.keys() or content[key] is None or content[key] == "":
            error_message = f"Missing '{key}' in your JSON!"
            await self.send_json(
                {
                    "type": "system_message",
                    "error": error_message
                }
            )
            return None
        else:
            return content[key]

    async def receive_json(self, content, **kwargs):
        message_type = await self.get_key(content, "type")

        if message_type == "new_ticket":
            # only users can create tickets
            await self.handle_new_ticket(content)
        elif message_type == "close_ticket":
            # only users can close tickets
            await self.handle_close_ticket()
        elif message_type == "new_message":
            await self.handle_new_message(content)

    async def handle_new_ticket(self, content):
        if self.is_specialist:
            error_message = "You are a specialist and cannot create a ticket!"
            await self.send_json(
                {
                    "type": "system_message",
                    "error": error_message
                }
            )
            return
        elif await database_sync_to_async(Ticket.objects.filter(user=self.user, is_closed=False).exists)():
            error_message = "You already have an active ticket!"
            await self.send_json(
                {
                    "type": "system_message",
                    "error": error_message
                }
            )
            return
        else:
            title = await self.get_key(content, "title")
            if title is None:
                return
            await database_sync_to_async(Ticket.objects.create)(user=self.user, title=title)

            # success message to the group
            await self.channel_layer.group_send(self.room_group_name, {
                "type": "system_message",
                "message": "Ticket created successfully!"
            })

    async def handle_close_ticket(self):
        if self.is_specialist:
            error_message = "You are a specialist and cannot close a ticket!"
            await self.send_json(
                {
                    "type": "system_message",
                    "error": error_message
                }
            )
            return
        elif not await database_sync_to_async(Ticket.objects.filter(user=self.user, is_closed=False).exists)():
            error_message = "You don't have an active ticket!"
            await self.send_json(
                {
                    "type": "system_message",
                    "error": error_message
                }
            )
            return
        else:
            ticket = await database_sync_to_async(Ticket.objects.get)(user=self.user, is_closed=False)
            ticket.is_closed = True
            await database_sync_to_async(ticket.save)()

            # success message to the group
            await self.channel_layer.group_send(self.room_group_name, {
                "type": "system_message",
                "message": "Ticket closed successfully!"
            })

    async def handle_new_message(self, content):
        message = await self.get_key(content, "message")
        if message is None:
            return

        # Send message to room group
        send_type = "user_message" if not self.is_specialist else "specialist_message"
        await self.channel_layer.group_send(
            self.room_group_name, {
                "type": send_type,  # This is the name of the method that will be called on the consumers
                "message": message
            }
        )

    async def user_message(self, event):
        await self.send_json(event)

    async def specialist_message(self, event):
        await self.send_json(event)

    async def system_message(self, event):
        await self.send_json(event)


class NotificationConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.group_name = 'specialists'
        self.user = None

    async def connect(self):
        self.user = self.scope['user']
        is_specialist = await database_sync_to_async(Specialist.objects.filter(user=self.user).exists)()

        if not is_specialist:
            error_message = "You are not a specialist!"
            raise DenyConnection(error_message)

        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()
        await self.send(text_data=json.dumps({
            "type": "system_message",
            "message": "You have successfully connected to the ticket notification group!"
        }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def system_message(self, event):
        await self.send(text_data=json.dumps(event))
