from django.urls import path
from .views import CustomMemberCreate, BlacklistUpdate, CurrentUserView

app_name = 'users'

urlpatterns = [
    path('register/', CustomMemberCreate.as_view(), name='register_new_user'),
    path('logout/', BlacklistUpdate.as_view(), name='blacklist'),
    path('userinfo/', CurrentUserView.as_view(), name='user_info')
]
