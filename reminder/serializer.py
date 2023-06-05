# from rest_framework import serializers
# from datetime import datetime
#
# class atendeesSerializer(serializers.Serializer):
#     email = serializers.EmailField(required=True)
#
# class timeSerializer(serializers.Serializer):
#     dateTime = serializers.DateTimeField(required=False, default=datetime.now())
#     timeZone = serializers.CharField(required=False, default="Asia/Tehran")
#
# class overrideSerializer(serializers.Serializer):
#     method = serializers.ChoiceField(required=True,
#         choices=['email', 'popup']
#     )
#     minutes = serializers.IntegerField(required=True)
#
# class reminderSerializer(serializers.Serializer):
#     useDefault = serializers.BooleanField(required=True)
#     overrides = overrideSerializer(required=False, default=[], many=True)
#
# class EventSerializer(serializers.Serializer):
#     summary = serializers.CharField(required=True)
#     location = serializers.CharField(required=False, default=None)
#     description = serializers.CharField(required=False, default=None)
#     start = timeSerializer(required=False, many=False)
#     end = timeSerializer(required=False, many=False)
#     recurrence = serializers.ListField(required=False, default=[],
#         child = serializers.CharField(required=True)
#     )
#     atendees = atendeesSerializer(required=False, default=[], many=True)
#
#     reminders = reminderSerializer(required=False,default=None, many=False)
