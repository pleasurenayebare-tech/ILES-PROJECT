from django.contrib.auth import get_user_model,update_session_auth_hash
from rest_framework import generics , permission ,status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken 
from .serializers import RegisterSerializer , UserSerializer 
from .permissions import IsAdminRole
User=get_user_model
class Registerview(generics.CreateAPIView):
      querryset=User.objects.all()
      serializer_class =     RegisterSerializer 
      permission_class = [permissions.AllowAny]
class CurrentUserView(APIView):
      permission_classes =    [permissions.IsAunthenticated]
      def get_object(self):
          return self.request.user
class UpdateProfileView(generics.UpdateAPIView):
      serializer_class = UserSerializer 
      permission_classes = [permissions.IsAuthenticated]
      def get_object(self):
          return self.request.user
class ChangePasswordView(APIView):
      permission_classes = [permissions.IsAuthenticated]
      def post(self,request):
          user = request.user
          old_password = request.data.get("old_password")
          new_password = request.data.get("new_password")
          if not old_password or not new_password:
             return Response(
                  {"error": "Both old and new password are required."}, status=status.HTTP_400_BAD_REQUEST
             )
          if not user.check_password(old_password):
             return Response(
                  {"error":"Old password is incorrect."},status=status.HTTP_400_BAD_REQUEST 
             )
          user.set_password(newpassword)
          user.save()
    update_session_auth_hash(request,user)
          return Response ({"message":"Password updated successfully.}) 
class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdminRole]
    def get_queryset(self):
        role = self.request.query_params.ger("role"
)
        if role:
            return User.objects.filter(role=role)
        return User.objects.all()
class LogoutView(APIView):
    permission _classes = [permissions.IsAuthenticated]
    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            if not refresh_token:
                return Response(
                    {"error":"Refresh token is required."},
                    status=status.HTTP 400 BAD_REQUEST
                )
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message":"Logged out successfully."})
except Exception:
    return Response(
        {"error":"Invalid or expired token."},
        status=status.HTTP_400_BAD_REQUEST
)