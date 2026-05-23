from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class AccountsModelTest(TestCase):
    """Test cases for the Accounts app models."""
    
    def setUp(self):
        """Set up test data before each test runs."""
        self.student = User.objects.create_user(
            username="teststudent",
            email="student@test.com",
            password="Test1234!",
            role="Student"
        )

    def test_user_created_successfully(self):
        """Test that a user is created with the correct username."""
    
