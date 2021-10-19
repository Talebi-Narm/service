from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainPage), 
    path('plants/', views.plantPage), 
    path('tools/', views.toolPage), 
    path('tags/', views.tagPage), 
]