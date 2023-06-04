from django.forms.models import model_to_dict
from rest_framework import serializers

from store.models import PlantComment, ToolComment


class PlantCommentSerializer(serializers.ModelSerializer):
    owner_detail = serializers.SerializerMethodField("get_owner")
    reply_to_detail = serializers.SerializerMethodField("get_reply_to")

    def get_owner(self, obj):
        return model_to_dict(obj.owner)

    def get_reply_to(self, obj):
        if obj.reply_to is None:
            return None
        return model_to_dict(obj.reply_to)

    class Meta:
        model = PlantComment
        fields = '__all__'
        read_only_fields = ['id', 'owner_detail', 'reply_to_detail']


class ToolCommentSerializer(serializers.ModelSerializer):
    owner_detail = serializers.SerializerMethodField("get_owner")
    reply_to_detail = serializers.SerializerMethodField("get_reply_to")

    def get_owner(self, obj):
        return model_to_dict(obj.owner)

    def get_reply_to(self, obj):
        if obj.reply_to is None:
            return None
        return model_to_dict(obj.reply_to)

    class Meta:
        model = ToolComment
        fields = '__all__'
        read_only_fields = ['id', 'owner_detail', 'reply_to_detail']
