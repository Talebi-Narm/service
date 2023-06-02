from rest_framework import serializers


class GoogleLoginSerializer(serializers.Serializer):
    id_token = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
