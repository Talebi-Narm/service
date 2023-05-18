from django.urls import re_path

from support import consumers

websocket_urlpatterns = [
    re_path(r"ws/v1/support/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
]
