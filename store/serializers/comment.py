from rest_framework import serializers

from store.models import PlantComment, ToolComment


class PlantCommentSerializer(serializers.ModelSerializer):
    owner_detail = serializers.SerializerMethodField("get_owner")
    reply_to_detail = serializers.SerializerMethodField("get_reply_to")

    def get_owner(self, obj):
        return obj.owner.id

    def get_reply_to(self, obj):
        if obj.reply_to is None:
            return None
        return obj.reply_to.id

    class Meta:
        model = PlantComment
        fields = '__all__'
        read_only_fields = ['id', 'owner_detail', 'reply_to_detail']


class ToolCommentSerializer(serializers.ModelSerializer):
    owner_detail = serializers.SerializerMethodField("get_owner")
    reply_to_detail = serializers.SerializerMethodField("get_reply_to")

    def get_owner(self, obj):
        return obj.owner.id

    def get_reply_to(self, obj):
        if obj.reply_to is None:
            return None
        return obj.reply_to.id

    class Meta:
        model = ToolComment
        fields = '__all__'
        read_only_fields = ['id', 'owner_detail', 'reply_to_detail']
