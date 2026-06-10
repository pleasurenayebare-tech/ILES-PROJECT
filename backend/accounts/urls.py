from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CurrentUserView, RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"), 
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    
    # Returns the profile data of the currently authenticated user
    # Requires a valid JWT access token in the Authorization header
    path("me/", CurrentUserView.as_view(), name="me"),
]
