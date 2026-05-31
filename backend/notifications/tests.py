from django.test import TestCase
from django.contrib.auth import get_user_model

from notifications.models import Notification
from notifications.utils import notify_user

User = get_user_model()


class NotificationsModelTest(TestCase):
  """Test cases for the Notification model.
