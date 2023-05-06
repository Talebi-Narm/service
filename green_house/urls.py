from django.urls import path

from . import apis

urlpatterns = [
    path('user-plants/', apis.UserPlantListAPIView.as_view(), name='user-plants'),
    path('user-plants/<uuid:pk>/', apis.UserPlantDetailAPIView.as_view(), name='user-plant-detail'),
]
