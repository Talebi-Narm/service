from rest_framework import serializers

from cart.models import PlantCart, ToolCart


class PlantCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantCart
        exclude = ["is_active", "is_deleted", "deleted_at", "created_at", "updated_at"]


class ToolCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolCart
        exclude = ["is_active", "is_deleted", "deleted_at", "created_at", "updated_at"]
