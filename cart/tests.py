import pytest
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken

from cart.models import PlantCart, ToolCart
from store.models import Plant, Tool
from user.models import User


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.mark.django_db
def test_plant_cart_create():
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

    plant_cart = PlantCart.objects.create(user=user, count=1, plant=plant)

    assert plant_cart.count == 1
    assert plant_cart.is_active == True


@pytest.mark.django_db
def test_plant_cart_detail_api(api_client):
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

    plant_cart = PlantCart.objects.create(user=user, count=1, plant=plant)

    api_name = 'plant-cart-detail'
    token = str(RefreshToken.for_user(user).access_token)
    random_uuid = '123e4567-e89b-12d3-a456-426614174000'
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    url = reverse(api_name, kwargs={'pk': random_uuid})
    response = api_client.get(url)
    assert response.status_code == 404

    url = reverse(api_name, kwargs={'pk': plant_cart.id})
    response = api_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_tool_cart_create():
    user = User.objects.create_user(username='test-user', password='test-password')
    tool = Tool.objects.create(
        name='test tool',
        description='Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        count=10,
        price=35,
        main_image='image tool'
    )

    tool_cart = ToolCart.objects.create(user=user, count=1, tool=tool)

    assert tool_cart.count == 1
    assert tool_cart.is_active == True


@pytest.mark.django_db
def test_order_detail_api(api_client):
    user = User.objects.create_user(username='test-user', password='test-password')
    tool = Tool.objects.create(
        name='test tool',
        description='Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        count=10,
        price=35,
        main_image='image tool'
    )

    tool_cart = PlantCart.objects.create(user=user, count=1, tool=tool)

    api_name = 'tool-cart-detail'
    token = str(RefreshToken.for_user(user).access_token)
    random_uuid = '123e4567-e89b-12d3-a456-426614174000'
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    url = reverse(api_name, kwargs={'pk': random_uuid})
    response = api_client.get(url)
    assert response.status_code == 404

    url = reverse(api_name, kwargs={'pk': tool.id})
    response = api_client.get(url)
    assert response.status_code == 200
