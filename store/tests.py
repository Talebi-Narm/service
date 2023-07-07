import pytest
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken

from store.models import Plant, Tool
from user.models import User


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.mark.django_db
def test_plant_create():
    plant = Plant.objects.create(
        name='test plant 1',
        description='Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        count=5,
        price=100,
        main_image='image1',
        environment=0,
        water=1,
        light=0,
        growth_rate=2
    )

    assert plant.name == 'test plant 1'
    assert plant.price == 100
    assert plant.environment == 0


@pytest.mark.django_db
def test_plant_detail_api(api_client):
    user = User.objects.create_user(username='test-user', password='test-password')
    plant = Plant.objects.create(
        name='test plant 1',
        description='Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        count=5,
        price=100,
        main_image='image1',
        environment=0,
        water=1,
        light=0,
        growth_rate=2
    )

    api_name = 'plants-detail'
    token = str(RefreshToken.for_user(user).access_token)
    random_uuid = '123e4567-e89b-12d3-a456-426614174000'
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    url = reverse(api_name, kwargs={'pk': random_uuid})
    response = api_client.get(url)
    assert response.status_code == 404

    url = reverse(api_name, kwargs={'pk': plant.id})
    response = api_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_tool_create():
    tool = Tool.objects.create(
        name='test tool',
        description='Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        count=10,
        price=35,
        main_image='image tool'
    )

    assert tool.name == 'test tool'
    assert tool.price == 35
    assert tool.main_image == 'image tool'


@pytest.mark.django_db
def test_tool_detail_api(api_client):
    user = User.objects.create_user(username='test-user', password='test-password')
    tool = Tool.objects.create(
        name='test tool',
        description='Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        count=10,
        price=35,
        main_image='image tool'
    )

    api_name = 'tools-detail'
    token = str(RefreshToken.for_user(user).access_token)
    random_uuid = '123e4567-e89b-12d3-a456-426614174000'
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    url = reverse(api_name, kwargs={'pk': random_uuid})
    response = api_client.get(url)
    assert response.status_code == 404

    url = reverse(api_name, kwargs={'pk': tool.id})
    response = api_client.get(url)
    assert response.status_code == 200
