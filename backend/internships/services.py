from django.core.mail import send_mail

from notifications.models import Notification


def notify_user(user, title, message):
    """
    Send a notification to a user via two channels:
    1. In-app notification stored in the database.
    2. Email notification (if the user has an email address).
    """

    # Create an in-app notification record in the database
    Notification.objects.create(
        user=user, 
        title=title, 
        message=message, 
        channel="in_app"
    )

    # Send an email notification if the user has a registered email
    if user.email:
        send_mail(
            subject=title,
            message=message,
            from_email=None,   # Uses DEFAULT_FROM_EMAIL from settings.py
            recipient_list=[user.email],
            fail_silently=True,   # Prevents email errors from crashing the app
        )

def notify_users(users, title, message):
    """
