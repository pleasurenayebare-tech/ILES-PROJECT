def validate(self, attrs):
    role = attrs.get("role")
    if role == "Student" and not attrs.get("student_number"):
        raise serializers.ValidationError({"student_number": "Required for students."})
    if role in ("WorkplaceSupervisor", "AcademicSupervisor") and not attrs.get("staff_number"):
        raise serializers.ValidationError({"staff_number": "Required for supervisors."})
    # your existing empty string logic...
    return attrs

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (...)

    def validate_password(self, value):
        validate_password(value)
        return value
        
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value
