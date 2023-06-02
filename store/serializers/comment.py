from rest_framework import serializers

from store.models import PlantComment, ToolComment


class PlantCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantComment
        fields = '__all__'


class ToolCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolComment
        fields = '__all__'
