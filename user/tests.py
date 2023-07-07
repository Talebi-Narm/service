import os
from datetime import datetime

import pytest
from PIL import Image
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.mark.django_db
def test_avatar_upload(api_client):
    user = User.objects.create_user(username='test-user', password='test-password')
    api_name = "user-avatar"  # noqa
    token = str(RefreshToken.for_user(user).access_token)
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
    url = '/api/v1/user/me/avatar/'

    # fail case
    response = api_client.put(url, {'avatar_url': 'test-avatar'}, format='multipart')
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    # success case
    file_name = datetime.now().strftime("%Y%m%d-%H%M%S") + '.png'
    Image.new('RGB', (100, 100)).save(file_name)
    with open(file_name, 'rb') as fp:
        response = api_client.put(url, {'avatar_url': fp}, format='multipart')
    os.remove(file_name)
    assert response.status_code == status.HTTP_200_OK
