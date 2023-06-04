from django.urls import re_path

from support import consumers

websocket_urlpatterns = [
    re_path(r"ws/v1/support/chat/(?P<room_name>[0-9a-f-]+)/$", consumers.ChatConsumer.as_asgi()),
    re_path(r'ws/v1/support/ticket/notifications/$', consumers.NotificationConsumer.as_asgi()),
]
