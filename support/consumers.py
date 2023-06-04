from channels.db import database_sync_to_async
from channels.exceptions import DenyConnection
from channels.generic.websocket import AsyncJsonWebsocketConsumer

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

    async def connect_specialist(self):
        pass

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def get_key(self, content, key):
        if key not in content.keys() or content[key] is None or content[key] == "":
            error_message = f"Missing '{key}' in your JSON!"
            await self.send_json(
                {"error": error_message}
            )
            return None
        else:
            return content[key]

    async def receive_json(self, content, **kwargs):
        message_type = await self.get_key(content, "type")

        if message_type == "new_ticket":
            await self.handle_new_ticket(content)
        elif message_type == "close_ticket":
            await self.handle_close_ticket()
        elif message_type == "new_message":
            await self.handle_new_message(content)

    async def handle_new_ticket(self, content):
        # check if user already has an active ticket
        if await database_sync_to_async(Ticket.objects.filter(user=self.user, is_closed=False).exists)():
            error_message = "You already have an active ticket!"
            await self.send_json(
                {"error": error_message}
            )
            return
        else:
            title = await self.get_key(content, "title")
            if title is None:
                return
            ticket = await database_sync_to_async(Ticket.objects.create)(user=self.user, title=title)
            await database_sync_to_async(ticket.save)()

    async def handle_close_ticket(self):
        # check if user has an active ticket
        if not await database_sync_to_async(Ticket.objects.filter(user=self.user, is_closed=False).exists)():
            error_message = "You don't have an active ticket!"
            await self.send_json(
                {"error": error_message}
            )
            return
        else:
            ticket = await database_sync_to_async(Ticket.objects.get)(user=self.user, is_closed=False)
            ticket.is_closed = True
            await database_sync_to_async(ticket.save)()

    async def handle_new_message(self, content):
        message = await self.get_key(content, "message")
        if message is None:
            return

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {
                "type": "new_message",  # This is the name of the method that will be called on the consumers
                "message": message
            }
        )

    async def new_message(self, event):
        await self.send_json(event)
