from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class AccountsModelTest(TestCase):
    """Test cases for the Accounts app models."""
    
    def setUp(self):
        """Set up test data before each test runs."""
        self.student = User.objects.create_user
            username="teststudent",
            email="student@test.com",
            password="Test1234!",
            role="Student"
        )

    def test_user_created_successfully(self):
        """Test that a user is created with the correct username."""
        self.assertEqual(self.student.username, "teststudent")

    def test_user_email(self):
        """Test that the user email is saved correctly."""
        self.assertEqual(self.student.email, "student@test.com")

    def test_user_role_is_student(self):
        """Test that user role is set to Student."""
        self.assertEqual(self.student.role, "Student")

    def test_user_is_active_by_default(self):
        """Test that a newly created user is active."""
        self.assertTrue(self.student.is_active)

    def test_user_is_not_staff_by_default(self):
        """Test that a newly created user is not a staff member."""
        self.assertFalse(self.student.is_staff)
        
