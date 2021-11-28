from django.urls import path
from . import views

urlpatterns = [
    path('reminder/', views.reminder, name='reminder'),
    path('deleteCreds/', views.deleteCreds, name='deleteCreds'),
    path('deleteCalendar/', views.deleteCalendar, name='deleteCalendar'),
]
