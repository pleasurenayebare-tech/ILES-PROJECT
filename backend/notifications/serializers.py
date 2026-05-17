from rest_framework import serializers

from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ("id","title","message","channel","isread","createdat")
        read_only_fields = ("user", "created_at")
