from django.contrib import admin

from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    """Admin configuration for the Notification model."""

    # Columns displayed in the notification list view
    list_display = ("user", "title", "channel", "is_read", "created_at")

    # Filters available in the right sidebar of the admin list view
    list_filter = ("is_read", "channel")

    # Fields that can be searched in the admin search bar
    search_fields = ("user_username", "title", "message")
