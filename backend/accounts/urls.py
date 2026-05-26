from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import CurrentUserView, RegisterView

# URL patterns for the accounts app
# All routes are prefixed with /api/auth/ from the main urls.py
urlpatterns = [
    # Register a new user account
    path("register/", RegisterView.as_view(), name="register"),

    # Login and receive access + refresh JWT tokens
    path("login/", TokenObtainPairView.as_view(), name="login"),

    # Refresh an expired access token using a valid refresh token
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # Get the currently authenticated user's profile
    path("me/", CurrentUserView.as_view(), name="me"),
]
