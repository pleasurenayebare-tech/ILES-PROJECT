from django.contrib import admin

from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    """Admin configuration for the Notification model."""

    # Columns displayed in the notification list view
    list_display = ("user", "title", "channel", "isread", "createdat")
