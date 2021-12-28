from django.urls import path
from . import views

app_name = 'specialist'

urlpatterns=[
    path('', views.apiOverview, name='api'),
    path('register/', views.CustomSpecialistCreate.as_view(), name='specialist-register'),
    path('all-primary/', views.GetAllSpecialistPrimaryInfo.as_view(), name='specialist-all-primary'),
    path('all-secondary/', views.GetAllSpecialistSecondaryInfo.as_view(), name='specialist-all-secondary'),
    path('primary/', views.GetThisSpecialistPrimaryInfo.as_view(), name='specialist-primary'),
    path('secondary/', views.GetThisSpecialistSecondaryInfo.as_view(), name='specialist-secondary'),
    path('secondary/<str:pk>/', views.GetSpecialistIdSecondaryInfo.as_view(), name='specialist-secondary-id'),
    path('primary/<str:pk>/', views.GetSpecialistIdPrimaryInfo.as_view(), name='specialist-secondary-id'),
    path('update-secondary/<str:pk>/', views.UpdateSpecialistInfo.as_view(), name='specialist-update-secondary'),
    path('update-primary/<str:pk>/', views.UpdatePrimarySpecialistInfo.as_view(), name='specialist-update-secondary'),
    path('delete/', views.RemoveSpecialist.as_view(), name='specialist-delete'),
]