from django.urls import path
from . import views

urlpatterns=[
    path('myPlants', views.allOfMyPlant, name='allOfMyPlants'),
    path('addToMyPlants', views.addPlantToMyGreenHouse, name='addPlantToMyGreenHouse'),
    path('updateInMyPlants/<str:pk>/', views.updatePlantInMyGreenHouse, name='updatePlantInMyGreenHouse'), 
]