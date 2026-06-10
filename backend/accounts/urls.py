from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# CurrentUserView: returns the profile of the currently logged-in user
# RegisterView: handles new user account registration
from .views import CurrentUserView, RegisterView
# URL patterns for the accounts app
# All routes are prefixed with /api/auth/ as defined in the main config/urls.py

urlpatterns = [
    # POST /api/auth/register/
    # Accepts new user registration data and creates an account
    # No authentication required — open to all users
    path("register/", RegisterView.as_view(), name="register"),
    # POST /api/auth/login/
    # Accepts username and password, returns JWT access and refresh tokens
    # No authentication required — open to all users
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
