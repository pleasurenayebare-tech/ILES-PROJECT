from django.test import TestCase
from django.contrib.auth import get_user_model

from notifications.models import Notification
from notifications.utils import notify_user

User = get_user_model()


class NotificationsModelTest(TestCase):
    """Test cases for the Notification model."""
  
    def setUp(self):
        """Set up a test user before each test runs."""
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@test.com",
            password="Test1234!",
        )

    def test_notification_created_successfully(self):
        """Test that a notification is created and saved to the database."""
        notification = Notification.object.create(
            user=self.user,
            title="Test Notification",
            message="This is a test message.",
            channel="in_app"
        )
        self.assertEqual(Notification.objects.count(), 1)
        self.assertEqual(notification.title, "Test Notification")

    def test_notification_is_unread_by_default(self):
        """Test that a newly created notification is unread by default."""
        notification = Notification.objects.create(
            user=self.user,
            title="Unread Test",
            message="This should be unread",
            channel="in_app"
        )
        self.assertFalse(notification.is_read)

    def test_notification_belongs_to_correct_user(self):
        """Test that the notification is linked to the correct user."""
        notification = Notification.objects.create(
            user=self.user,
            title="User Test",
            message="Belongs to testuser.",
            channel="in_app"
        )
        self.assertEqual(notification.user.username, "testuser")

    def test_notify_user_creates_notification(self):
