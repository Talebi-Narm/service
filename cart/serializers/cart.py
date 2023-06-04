from django.forms.models import model_to_dict
from rest_framework import serializers

from cart.models import PlantCart, ToolCart


class PlantCartSerializer(serializers.ModelSerializer):
    plant_detail = serializers.SerializerMethodField("get_plant")

    def get_plant(self, obj):
        return model_to_dict(obj.plant)

    class Meta:
        model = PlantCart
        exclude = ["is_active", "is_deleted", "deleted_at", "created_at", "updated_at"]
        read_only_fields = ['id', 'plant_detail']


class ToolCartSerializer(serializers.ModelSerializer):
    tool_detail = serializers.SerializerMethodField("get_tool")

    def get_tool(self, obj):
        return model_to_dict(obj.tool)

    class Meta:
        model = ToolCart
        exclude = ["is_active", "is_deleted", "deleted_at", "created_at", "updated_at"]
        read_only_fields = ['id', 'tool_detail']
