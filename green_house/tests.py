import pytest
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import User
from .models import UserPlant


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.mark.django_db
def test_user_plant_create():
    user = User.objects.create_user(username='test-user', password='test-password')
    user_plant = UserPlant.objects.create(
        user=user,
        nickname='test-user-plant'
    )

    assert user_plant.nickname == 'test-user-plant'
    assert user_plant.user_id == user.id
    assert user_plant.is_active is True
    assert user_plant.is_deleted is False


@pytest.mark.django_db
def test_user_plant_detail_api(api_client):
    user = User.objects.create_user(username='test-user', password='test-password')
    user_plant = UserPlant.objects.create(
        user=user,
        nickname='test-user-plant'
    )
    api_name = 'user-plants-detail'
    token = str(RefreshToken.for_user(user).access_token)
    random_uuid = '123e4567-e89b-12d3-a456-426614174000'
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    url = reverse(api_name, kwargs={'pk': random_uuid})
    response = api_client.get(url)
    assert response.status_code == 404

    url = reverse(api_name, kwargs={'pk': user_plant.id})
    response = api_client.get(url)
    assert response.status_code == 200
