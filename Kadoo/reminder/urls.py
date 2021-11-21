from django.urls import path
from . import views

urlpatterns = [
    path('reminder/', views.reminder, name='reminder'),
]
