from rest_framework_simplejwt import views

from django.urls import path

app_name = 'users'

urlpatterns = [
    path("jwt/create/", views.TokenObtainPairView.as_view(), name="jwt-create"),
    path("jwt/refresh/", views.TokenRefreshView.as_view(), name="jwt-refresh"),
    # path('', views.apiOverview, name='api'),
    # path('register/', CustomMemberCreate.as_view(), name='register_new_user'),
    # path('updatecredit/<int:amount>/', UpdateCredit.as_view(), name='update_credit'),
    # path('logout/', BlacklistUpdate.as_view(), name='blacklist'),
    # path('userinfo/', CurrentUserView.as_view(), name='user_info'),
    # path('userinfo/<int:pk>/', IDUserView.as_view(), name='user_info_id'),
]
