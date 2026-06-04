from django.apps import AppConfig


class NotificationsConfig(AppConfig):
    """Configuration class for the Notifications application."""

    # Default field type for auto-generated primary keys
    default_auto_field = "django.db.models.BigAutoField"

    # The name of the app as recognised by Django
    name = "notifications"
