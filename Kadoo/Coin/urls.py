from django.urls import path
from . import views

app_name = 'coin'

urlpatterns=[
    path('', views.apiOverview, name='api'),

    path('upadte-value/', views.UpdateThisUserCoin.as_view(), name='upadte-value'),
    path('update-value/<str:pk>/', views.UpdateUserCoinWithId.as_view(), name='update-value-id'),
    path('add-value/', views.AddThisUserCoin.as_view(), name='add-value'),
    path('add-value-id/', views.AddUserCoinWithId.as_view(), name='add-value-id'),
    path('reduce-value/', views.ReduceThisUserCoin.as_view(), name='reduce-value'),
    path('reduce-value-id/', views.ReduceUserCoinWithId.as_view(), name='reduce-value-id'),
    path('get-all/', views.GetTAllCoin.as_view(), name='get-all'),
    path('get/', views.GetThisUserCoin.as_view(), name='get'),
    path('get/<str:pk>/', views.GetUserCoinWithId.as_view(), name='get-id'),
]