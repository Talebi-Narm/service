import pytest

from common.models import PlantBookmark, ToolBookmark
from store.models import Plant, Tool
from user.models import User


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.mark.django_db
def test_plant_bookmark_create():
    user = User.objects.create_user(username='test-user', password='test-password')
    plant = Plant.objects.create(
        name='test-plant',
        description='test-plant-description',
        price=1000,
        count=100,
        is_active=True
    )
    plant_bookmark = PlantBookmark.objects.create(
        user=user,
        Plant=plant,
    )

    assert plant_bookmark.user_id == user.id
    assert plant_bookmark.Plant == plant


@pytest.mark.django_db
def test_tool_bookmark_create():
    user = User.objects.create_user(username='test-user', password='test-password')
    tool = Tool.objects.create(
        name='test-tool',
        description='test-tool-description',
        price=1000,
        count=100,
        is_active=True
    )
    tool_bookmark = ToolBookmark.objects.create(
        user=user,
        Tool=tool,
    )

    assert tool_bookmark.user_id == user.id
    assert tool_bookmark.Tool == tool
