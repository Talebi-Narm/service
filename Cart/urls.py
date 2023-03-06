from django.urls import path
from .views import AddPlantToCart, AddToolToCart, ApproveAllInCart, GetAllPlantsCart, GetAllToolsCart, GetApprovedPlantsCart, GetApprovedToolsCart, GetCountCart, GetPriceCart, GetUnapprovedPlantsCart, GetUnapprovedPlantsCartWithCount, GetUnapprovedToolsCart, GetUnapprovedToolsCartWithCount, RemoveAllPlantsFromCart, RemoveAllToolsFromCart, RemovePlantFromCart, RemoveToolFromCart, UpdatePlantToCart, UpdateToolToCart
from . import views

app_name = 'cart'

urlpatterns=[
    path('', views.apiOverview, name='api'),
    path('add-plant-to-cart/', AddPlantToCart.as_view(), name='add-plant-to-cart'),
    path('add-tool-to-cart/', AddToolToCart.as_view(), name='add-tool-to-cart'),
    path('user-all-plants/', GetAllPlantsCart.as_view(), name='user-all-plants'),
    path('user-all-tools/', GetAllToolsCart.as_view(), name='user-all-tools'),
    path('user-unapproved-plants-cart/', GetUnapprovedPlantsCart.as_view(), name='user-unapproved-plants-cart'),
    path('user-unapproved-tools-cart/', GetUnapprovedToolsCart.as_view(), name='user-unapproved-tools-cart'),
    path('user-unapproved-plants-cart-count/', GetUnapprovedPlantsCartWithCount.as_view(), name='user-unapproved-plants-cart-count'),
    path('user-unapproved-tools-cart-count/', GetUnapprovedToolsCartWithCount.as_view(), name='user-unapproved-tools-cart-count'),
    path('user-approved-plants-cart/', GetApprovedPlantsCart.as_view(), name='user-approved-plants-cart'),
    path('user-approved-tools-cart/', GetApprovedToolsCart.as_view(), name='add-plant-to-cart'),
    path('user-price-cart/', GetPriceCart.as_view(), name='user-price-cart'),
    path('user-count-cart/', GetCountCart.as_view(), name='user-count-cart'),
    path('update-plant-cart/', UpdatePlantToCart.as_view(), name='update-plant-cart'),
    path('update-tool-cart/', UpdateToolToCart.as_view(), name='update-tool-cart'),
    path('delete-plant-cart/', RemovePlantFromCart.as_view(), name='delete-plant-cart'),
    path('delete-tool-cart/', RemoveToolFromCart.as_view(), name='delete-tool-cart'),
    path('delete-all-plant-cart/', RemoveAllPlantsFromCart.as_view(), name='delete-all-plant-cart'),
    path('delete-all-tool-cart/', RemoveAllToolsFromCart.as_view(), name='delete-all-tool-cart'),
    path('approve-all-cart/', ApproveAllInCart.as_view(), name='approve-all-cart'),
]