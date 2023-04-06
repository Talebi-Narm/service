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
        path('store/', include('store.urls')),
        path('green_house/', include('green_house.urls')),
        path('reminder/', include('reminder.urls')),
        path('auth/', include('rest_framework.urls', namespace='rest_framework_CHANGE_THIS')),
        path('user/', include('user.urls', namespace='users')),
        path('cart/', include('cart.urls', namespace='cart')),
        path('specialist/', include('specialist.urls', namespace='specialist')),
        path('ticket', include('ticket.urls', namespace='ticket')),
        path('coin', include('coin.urls', namespace='coin')),
        path('token-auth/', AuthTokenView.as_view()),

        path('schema/', SpectacularAPIView.as_view(), name='schema'),
        path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
        path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc')
    ]))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
