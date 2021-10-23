from django.urls import path
from .views import AddPlantToCart
from . import views

app_name = 'cart'

urlpatterns=[
    path('', views.apiOverview, name='api'),
# Cart Plant API
    path('add-plant-to-cart/', AddPlantToCart.as_view(), name='add-plant-to-cart'),
]