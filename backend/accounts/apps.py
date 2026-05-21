from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """Configuration class for the Accounts application."""
    
    # Default feild type for auto-generated primary keys
    default_auto_field = "django.db.models.BigAutoField"
    name = 'accounts'
