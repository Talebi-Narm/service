import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = 'test_group'
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )

        self.accept()
        # self.send(text_data=json.dumps({
        #     'type': 'connection established',
        #     'message': 'Hello World!'
        # }))

    def disconnect(self, close_code):
        pass
        # self.send(text_data=json.dumps({
        #     'type': 'connection closed',
        #     'message': 'Goodbye World!'
        # }))

    def receive(self, text_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # print("message:", message)
        # self.send(text_data=json.dumps({
        #     'type': 'chat',
        #     'message': message
        # }))
        async_to_sync(self.channel_layer.group_send)(
            self.group_name, {
                'type': 'chat_message',
                'message': message
            }
        )

    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message
        }))
