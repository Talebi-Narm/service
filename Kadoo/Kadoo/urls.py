from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import generics

class AuthTokenView(ObtainAuthToken, generics.GenericAPIView):
    pass

schema_view = get_swagger_view(title='Kadoo Project Swagger')

urlpatterns = [
    path('', include('Backend.urls')),
    path('swagger/', schema_view),
    path('accounts/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('Backend_API.urls')),
    path('api/', include('Green_House.urls')),
    path('api/', include('Reminder.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/user/', include('Users.urls', namespace='users')),
    path('api/cart/', include('Cart.urls', namespace='cart')),
    path('api/specialist/', include('Specialist.urls', namespace='specialist')),
    path('api/ticket/', include('Ticket.urls', namespace='ticket')),
    path('api/coin/', include('Coin.urls', namespace='coin')),
    path(r'^api-token-auth/', AuthTokenView.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)