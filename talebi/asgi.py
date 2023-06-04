import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from support.middleware import TokenAuthMiddleware
from support.urls import ws

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'talebi.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": TokenAuthMiddleware(
        URLRouter(
            ws.websocket_urlpatterns
        )
    )
})
