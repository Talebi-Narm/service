from rest_framework.serializers import ModelSerializer
from .models import UserPlant


class UserPlantSerializer(ModelSerializer):
    class Meta:
        model = UserPlant
        read_only_fields = ('id',)
        exclude = ('is_deleted', 'deleted_at')
