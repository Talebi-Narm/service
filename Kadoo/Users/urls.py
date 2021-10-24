from django import urls
from django.urls import path
from .views import CustomMemberCreate, BlacklistUpdate, CurrentUserView, UpdateCredit
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


app_name = 'users'

urlpatterns = [
    path('', views.apiOverview, name='api'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', CustomMemberCreate.as_view(), name='register_new_user'),
    path('updatecredit/<int:amount>/', UpdateCredit.as_view(), name='update_credit'),
    path('logout/', BlacklistUpdate.as_view(), name='blacklist'),
    path('userinfo/', CurrentUserView.as_view(), name='user_info'),
]
