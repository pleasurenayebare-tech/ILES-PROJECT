from django.urls import path
# JWT authentication views from SimpleJWT library
# TokenObtainPairView: handles login and returns access + refresh tokens
# TokenRefreshView: handles refreshing an expired access token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# Custom views defined in this app's views.py
# CurrentUserView: returns the profile of the currently logged-in user
# RegisterView: handles new user account registration
from .views import CurrentUserView, RegisterView
# URL patterns for the accounts app
# All routes are prefixed with /api/auth/ as defined in the main config/urls.py

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("me/", CurrentUserView.as_view(), name="me"),
]
