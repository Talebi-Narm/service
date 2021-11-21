from rest_framework import serializers
import datetime

class timeSerializer(serializers.Serializer):
    time = serializers.DateTimeField(required=False, default=datetime.datetime.now())
    timeZone = serializers.CharField(required=False, default='Asia/Tehran')

class EventSerializer(serializers.Serializer):
    summary = serializers.CharField(required=True)
    description = serializers.CharField(required=False, default=None)
    startTime = timeSerializer(many=False)
    endTime = timeSerializer(many=False)
    recurrence = serializers.ListField(required=False, default=[],
        child = serializers.CharField(required=True)
    )
    atendees = serializers.ListField(required=False, default=[],
        child = serializers.EmailField(required=True)
    )

class overrideSerializer(serializers.Serializer):
    method = serializers.ChoiceField(required=True,
        choices=['email', 'popup']
    )
    minutes = serializers.IntegerField(required=True)

class reminderSerializer(serializers.Serializer):
    useDefault = serializers.BooleanField(required=True)
    overrides = serializers.ListField(required=False, default=[]
        child = overrideSerializer(many=True)
    )