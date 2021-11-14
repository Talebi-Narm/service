from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('Backend.urls')),
    
    path('admin/', admin.site.urls),
    path('api/', include('Backend_API.urls')),
    path('api/', include('Green_House.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/user/', include('Users.urls', namespace='users')),
    path('api/cart/', include('Cart.urls', namespace='cart')),
    path('api/specialist/', include('Specialist.urls', namespace='specialist')),
    path('api/ticket/', include('Ticket.urls', namespace='specialist')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)