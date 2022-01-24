from django.urls import path
from . import views

urlpatterns=[
    path('makeHaveCalendarTrue/<str:pk>/', views.haveCalendarTrue.as_view(), name='makeHaveCalendarTrue'),
    path('myPlants/', views.allOfMyPlant.as_view(), name='allOfMyPlants'),
    path('myArchivedPlants/', views.allOfMyArchivedPlant.as_view(), name='allOfMyArchivedPlants'),
    path('myPlantsRUD/<str:pk>/', views.myPlantsRUD.as_view(), name='getPlant'),
]