from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """Configuration class for the Accounts application."""
    
    # Default feild type for auto-generated primary keys
    default_auto_field = "django.db.models.BigAutoField"
    
    # The name of the app as recognised by Django
    name = "accounts"
    def ready(self):
        """Called when the app is fully loaded."""
        pass
