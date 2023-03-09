from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken


class AuthTokenView(ObtainAuthToken, generics.GenericAPIView):
    pass


urlpatterns = [
    path('accounts/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('core/', include('core.urls')),
    path('green-house/', include('Green_House.urls')),
    path('reminder/', include('Reminder.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework_CHANGE_THIS')),
    path('user/', include('Users.urls', namespace='users')),
    path('cart/', include('Cart.urls', namespace='cart')),
    path('specialist/', include('Specialist.urls', namespace='specialist')),
    path('ticket/', include('Ticket.urls', namespace='ticket')),
    path('coin/', include('Coin.urls', namespace='coin')),
    path('api-token-auth/', AuthTokenView.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
