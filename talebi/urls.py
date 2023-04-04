from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken


class AuthTokenView(ObtainAuthToken, generics.GenericAPIView):
    pass


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include([
        path('Backend', include('Backend.urls')),
        path('Backend_API/', include('Backend_API.urls')),
        path('Green_House/', include('Green_House.urls')),
        path('Reminder/', include('Reminder.urls')),
        path('auth/', include('rest_framework.urls', namespace='rest_framework_CHANGE_THIS')),
        path('Users/', include('user.urls', namespace='users')),
        path('Cart/', include('Cart.urls', namespace='cart')),
        path('Specialist/', include('Specialist.urls', namespace='specialist')),
        path('Ticket', include('Ticket.urls', namespace='ticket')),
        path('Coin', include('Coin.urls', namespace='coin')),
        path('token-auth/', AuthTokenView.as_view()),

        path('schema/', SpectacularAPIView.as_view(), name='schema'),
        path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
        path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc')
    ]))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
