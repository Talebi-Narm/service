from django.urls import path
from . import views

app_name = 'ticket'

urlpatterns=[
    path('', views.apiOverview, name='api'),

    path('new-question-ticket/', views.QuestionTicketCreateForNewConversation.as_view(), name='new-question-ticket'),
    path('new-question-ticket/<str:pk>/', views.QuestionTicketCreateForGivenConversation.as_view(), name='new-question-ticket'),
    path('new-answer-ticket/<str:pk>/', views.AnswerTicketCreateForGivenConversation.as_view(), name='new-answer-ticket'),
    path('all-conversations/', views.GetAllConversations.as_view(), name='all-conversations'),
    path('all-tickets/', views.GetAllTickects.as_view(), name='all-tickets'),
    path('member-conversations/', views.GetThisUserConversations.as_view(), name='member-conversations'),
    path('specialist-conversations/', views.GetSpecialistConversations.as_view(), name='specialist-conversations'),
    path('member-conversations/<str:pk>/', views.GetUserConversations.as_view(), name='member-conversations'),
    path('specialist-conversations/<str:pk>/', views.GetSpecialistConversations.as_view(), name='specialist-conversations'),
    path('member-tickets/', views.GetThisUserTickets.as_view(), name='member-tickets'),
    path('specialist-tickets/', views.GetThisUserTickets.as_view(), name='specialist-tickets'),
    path('member-tickets/<str:pk>/', views.GetUserTickets.as_view(), name='member-tickets'),
    path('specialist-tickets/<str:pk>/', views.GetSpecialistTickets.as_view(), name='specialist-tickets'),
    path('rate-conversation/<str:pk>/', views.DoneTheConverstion.as_view(), name='rate-conversation'),
]