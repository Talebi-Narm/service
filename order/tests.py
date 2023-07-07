import pytest
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken

from cart.models import PlantCart, ToolCart
from order.models import Order
from store.models import Plant, Tool
from user.models import User


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.mark.django_db
def test_order_create():
    user = User.objects.create_user(username='test-user', password='test-password')
    plant1 = Plant.objects.create(
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
    plant2 = Plant.objects.create(
        name='test plant 2',
        description='Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        count=7,
        price=15,
        main_image='image2',
        environment=1,
        water=2,
        light=2,
        growth_rate=0
    )
    tool = Tool.objects.create(
        name='test tool',
        description='Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        count=10,
        price=35,
        main_image='image tool'
    )

    plant_cart1 = PlantCart.objects.create(user=user, count=1, plant=plant1)
    plant_cart2 = PlantCart.objects.create(user=user, count=2, plant=plant2)
    tool_cart = ToolCart.objects.create(user=user, count=3, tool=tool)

    order = Order.objects.create(
        user=user
    )
    order.plants.add(plant_cart1)
    order.plants.add(plant_cart2)
    order.tools.add(tool_cart)

    assert order.plants.count() == 2
    assert order.tools.count() == 1


@pytest.mark.django_db
def test_order_detail_api(api_client):
    user = User.objects.create_user(username='test-user', password='test-password')
    plant1 = Plant.objects.create(
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
    plant2 = Plant.objects.create(
        name='test plant 2',
        description='Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        count=7,
        price=15,
        main_image='image2',
        environment=1,
        water=2,
        light=2,
        growth_rate=0
    )
    tool = Tool.objects.create(
        name='test tool',
        description='Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        count=10,
        price=35,
        main_image='image tool'
    )

    plant_cart1 = PlantCart.objects.create(user=user, count=1, plant=plant1)
    plant_cart2 = PlantCart.objects.create(user=user, count=2, plant=plant2)
    tool_cart = ToolCart.objects.create(user=user, count=3, tool=tool)

    order = Order.objects.create(
        user=user
    )
    order.plants.add(plant_cart1)
    order.plants.add(plant_cart2)
    order.tools.add(tool_cart)

    api_name = 'order-detail'
    token = str(RefreshToken.for_user(user).access_token)
    random_uuid = '123e4567-e89b-12d3-a456-426614174000'
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    url = reverse(api_name, kwargs={'pk': random_uuid})
    response = api_client.get(url)
    assert response.status_code == 404

    url = reverse(api_name, kwargs={'pk': order.id})
    response = api_client.get(url)
    assert response.status_code == 200
