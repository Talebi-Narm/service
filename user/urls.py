from django.urls import path
from rest_framework_simplejwt import views

from user.apis.address import UserAddressList, UserAddressDetail
from user.apis.register import RegisterUserAPIView

app_name = 'users'

urlpatterns = [
    path("jwt/create/", views.TokenObtainPairView.as_view(), name="jwt-create"),
    path("jwt/refresh/", views.TokenRefreshView.as_view(), name="jwt-refresh"),
    path("register", RegisterUserAPIView.as_view(), name="new-user-register"),
    path("address", UserAddressList.as_view(), name="user-address-list"),
    path("address/<uuid:pk>", UserAddressDetail.as_view(), name="user-address-detail"),

    # path('', views.apiOverview, name='api'),
    # path('updatecredit/<int:amount>/', UpdateCredit.as_view(), name='update_credit'),
    # path('logout/', BlacklistUpdate.as_view(), name='blacklist'),
    # path('userinfo/', CurrentUserView.as_view(), name='user_info'),
    # path('userinfo/<int:pk>/', IDUserView.as_view(), name='user_info_id'),
]
