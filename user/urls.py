from django.urls import path
from rest_framework_simplejwt import views

from user.apis.address import UserAddressList, UserAddressDetail
from user.apis.google import GoogleLogin
from user.apis.register import RegisterUserAPIView, ChangePassword
from user.apis.user import UserProfile

app_name = 'users'

urlpatterns = [
    path("jwt/create/", views.TokenObtainPairView.as_view(), name="jwt-create"),
    path("jwt/refresh/", views.TokenRefreshView.as_view(), name="jwt-refresh"),
    path("register", RegisterUserAPIView.as_view(), name="new-user-register"),
    path("google-login", GoogleLogin.as_view(), name="google-login"),
    path("addresses", UserAddressList.as_view(), name="user-address-list"),
    path("addresses/<uuid:pk>", UserAddressDetail.as_view(), name="user-address-detail"),
    # path('updatecredit/<int:amount>/', UpdateCredit.as_view(), name='update_credit'),
    path("me/", UserProfile.as_view(), name="user-profile"),
    path("change-password/", ChangePassword.as_view(), name="change-password")
]
