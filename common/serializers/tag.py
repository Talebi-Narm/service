from rest_framework import serializers
from common.models import Tag

class TagAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        exclude = ['is_active', 'created_at', 'updated_at', 'is_deleted', 'deleted_at']

