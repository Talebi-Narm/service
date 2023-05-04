from django.urls import path

from cart.apis import cart as cart_views

app_name = 'cart'

urlpatterns = [
    path('plant-cart', cart_views.PlantCartList.as_view(), name="plant-cart"),
    path('plant-cart/<uuid:pk>/', cart_views.PlantCartList.as_view(), name="plant-cart"),
    path('tool-cart', cart_views.ToolCartList.as_view(), name="tool-cart"),
    path('tool-cart/<uuid:pk>/', cart_views.ToolCartList.as_view(), name="tool-cart"),
]
