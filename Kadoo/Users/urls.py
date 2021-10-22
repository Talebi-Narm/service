from django import urls
from django.urls import path
from .views import AddPlantToCart, CustomMemberCreate, BlacklistUpdate, CurrentUserView, UpdateCredit
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', CustomMemberCreate.as_view(), name='register_new_user'),
    path('updatecredit/<int:amount>/', UpdateCredit.as_view(), name='update_credit'),
    path('logout/', BlacklistUpdate.as_view(), name='blacklist'),
    path('userinfo/', CurrentUserView.as_view(), name='user_info'),
    path('addplant/', AddPlantToCart.as_view(), name='add_to_cart_plant'),
    #urls(r'^updatecredit/<int:amount>/', views.updateCredit)
]
