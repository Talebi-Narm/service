from django.forms.models import model_to_dict
from rest_framework import serializers

from store.models import Plant, Tool


class PlantAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'
        read_only_fields = ['id']


class PlantSerializer(serializers.ModelSerializer):
    tags_detail = serializers.SerializerMethodField("get_tags")

    def get_tags(self, obj):
        return [model_to_dict(tag, fields=['id', 'name', 'description']) for tag in obj.tags.all()]

    class Meta:
        model = Plant
        exclude = ['is_active', 'created_at', 'updated_at', 'is_deleted', 'deleted_at']
        read_only_fields = ['id', 'tags_detail']


class ToolAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = '__all__'
        read_only_fields = ['id']


class ToolSerializer(serializers.ModelSerializer):
    tags_detail = serializers.SerializerMethodField("get_tags")

    def get_tags(self, obj):
        return [model_to_dict(tag, fields=['id', 'name', 'description']) for tag in obj.tags.all()]

    class Meta:
        model = Tool
        exclude = ['is_active', 'created_at', 'updated_at', 'is_deleted', 'deleted_at']
        read_only_fields = ['id', 'tags_detail']
