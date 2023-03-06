from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken


class AuthTokenView(ObtainAuthToken, generics.GenericAPIView):
    pass


urlpatterns = [
    path('', include('Backend.urls')),
    path('accounts/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('Backend_API.urls')),
    path('api/', include('Green_House.urls')),
    path('api/', include('Reminder.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework_CHANGE_THIS')),
    path('api/user/', include('Users.urls', namespace='users')),
    path('api/cart/', include('Cart.urls', namespace='cart')),
    path('api/specialist/', include('Specialist.urls', namespace='specialist')),
    path('api/ticket/', include('Ticket.urls', namespace='ticket')),
    path('api/coin/', include('Coin.urls', namespace='coin')),
    path('api-token-auth/', AuthTokenView.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
