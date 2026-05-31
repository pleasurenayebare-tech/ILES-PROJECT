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
            password="Test1234!"
