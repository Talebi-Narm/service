from django.urls import path
from . import views

urlpatterns=[
    path('', views.apiOverview, name='api'),

# Plant API
    path('plantList/', views.plantList, name='plantList'),
    path('plantDetail/<str:pk>/', views.plantDetail, name='plantDetail'),
    path('createPlant/', views.createPlant, name='createPlant'),
    path('updatePlant/<str:pk>/', views.updatePlant, name='updatePlant'),
    path('deletePlant/<str:pk>/', views.deletePlant, name='deletePlant'),

# Tool API
    path('toolList/', views.toolList, name='toolList'),
    path('toolDetail/<str:pk>/', views.toolDetail, name='toolDetail'),
    path('createTool/', views.createTool, name='createTool'),
    path('updateTool/<str:pk>/', views.updateTool, name='updateTool'),
    path('deleteTool/<str:pk>/', views.deleteTool, name='deleteTool'),

# Tag API
    path('tagList/', views.tagList, name='tagList'),
    path('tagDetail/<str:pk>/', views.tagDetail, name='tagDetail'),
    path('createTag/', views.createTag, name='createTag'),
    path('updateTag/<str:pk>/', views.updateTag, name='updateTag'),
    path('deleteTag/<str:pk>/', views.deleteTag, name='deleteTag'),

]