from django.urls import re_path

from support import consumers

websocket_urlpatterns = [
    re_path(r"api/v1/support/chat/$", consumers.ChatConsumer.as_asgi()),
]
