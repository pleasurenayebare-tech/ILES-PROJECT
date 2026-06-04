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
    search_fields = ("user__username", "title", "message")

    # Order notifications by newest first
    ordering = ("-created_at",)

    # Make created_at read only since it is auto generated
    readonly_fields = ("created_at",)
