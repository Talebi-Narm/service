from rest_framework import serializers

from common.models import PlantBookmark, ToolBookmark


class PlantBookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantBookmark
        exclude = ['is_active', 'created_at', 'updated_at', 'is_deleted', 'deleted_at']
        read_only_fields = ['id']


class ToolBookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolBookmark
        exclude = ['is_active', 'created_at', 'updated_at', 'is_deleted', 'deleted_at']
        read_only_fields = ['id']
