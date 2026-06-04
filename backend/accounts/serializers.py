 def validate(self, attrs):
    """Cross-field validation to enforce role-specifc required fields."""
    role = attrs.get("role")
    
    # students must provide a students number
    if role == "Student" and not attrs.get("student_number"):
        raise serializers.ValidationError({"student_number": "Required for students."})
        
    # Workplace and Academic Supervisors must provide a staff number
    if role in ("WorkplaceSupervisor", "AcademicSupervisor") and not attrs.get("staff_number"):
        raise serializers.ValidationError({"staff_number": "Required for supervisors."})
        
    return attrs

class RegisterSerializer(serializers.ModelSerializer):
    """Serialiser for handling new user registration."""
    
    # Password is write-only so it is never returned in API responses
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (...
        read_only_fields = ("id", "role") # These fields are set by the system, not the user

    def validate_password(self, value):
        """Validate password strength usind Django's built-in validators."""
        validate_password(value)
        return value
        
    def validate_email(self, value):
        """Ensure the email address is not already registered in the system."""
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value
