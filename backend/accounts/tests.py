from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class AccountsModelTest(TestCase):
    """Test cases for the Accounts app models."""
    
    def setUp(self):
        """Set up test data before each test runs."""
        self.student = User.objects.create_user(
            username="teststudent",
            email="student@test.com"
