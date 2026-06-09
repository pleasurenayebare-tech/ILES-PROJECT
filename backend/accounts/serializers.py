from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Serializer for reading and updating user profile data."""

    class Meta:
        model = User
        fields = (
            "id", "username", "email", "first_name", "last_name",
            "role", "student_number", "staff_number", "phone_number", "department"
        )
        read_only_fields = ("id", "role")


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for handling new user registration."""

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "id", "username", "email", "first_name", "last_name",
            "password", "role", "student_number", "staff_number",
            "phone_number", "department"
        )
        read_only_fields = ("id",)

    def validate_password(self, value):
        """Validate password strength using Django's built-in validators."""
        validate_password(value)
        return value

    def validate_email(self, value):
        """Ensure the email address is not already registered in the system."""
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def validate(self, attrs):
        """Cross-field validation to enforce role-specific required fields."""
        role = attrs.get("role")

        if role == "Student" and not attrs.get("student_number"):
            raise serializers.ValidationError({"student_number": "Required for students."})

        if role in ("WorkplaceSupervisor", "AcademicSupervisor") and not attrs.get("staff_number"):
            raise serializers.ValidationError({"staff_number": "Required for supervisors."})

        return attrs

    def create(self, validated_data):
        """Create and return a new user with an encrypted password."""
        password = validated_data.pop("password")

        # Remove empty strings for unique fields to avoid constraint errors
        if not validated_data.get("student_number"):
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
