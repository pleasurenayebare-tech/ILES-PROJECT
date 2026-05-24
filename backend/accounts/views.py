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