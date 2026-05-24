from django.contrib.auth import get_user_model,update_session_auth_hash
from rest_framework import generics , permission ,status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken 