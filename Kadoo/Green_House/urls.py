from django.urls import path
from . import views

urlpatterns=[
    path('myPlants/', views.allOfMyPlant.as_view(), name='allOfMyPlants'),
    path('myArchivedPlants/', views.allOfMyArchivedPlant.as_view(), name='allOfMyArchivedPlants'),
    path('addToMyPlants/', views.addPlantToMyGreenHouse.as_view(), name='addPlantToMyGreenHouse'),
    path('MyPlants/<str:pk>/', views.myPlants.as_view(), name='getPlant'),
]