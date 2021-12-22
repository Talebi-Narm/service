from django.urls import path
from . import views

urlpatterns = [
    path('reminder/', views.reminder.as_view(), name='reminder'),
    path('deleteCreds/', views.deleteCreds.as_view(), name='deleteCreds'),
    path('deleteCalendar/', views.deleteCalendar.as_view(), name='deleteCalendar'),
]
