from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CurrentUserView, RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"), 
    # POST /api/auth/token/refresh/
    # Accepts a valid refresh token and returns a new access token
    # Used to keep the user logged in without re-entering credentials
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # GET /api/auth/me/
    # Returns the profile data of the currently authenticated user
    # Requires a valid JWT access token in the Authorization header
    path("me/", CurrentUserView.as_view(), name="me"),
]
