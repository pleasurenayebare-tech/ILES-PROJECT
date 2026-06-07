from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import CurrentUserView, RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),

    # Refresh an expired access token 
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # Get the currently authenticated user's profile
    path("me/", CurrentUserView.as_view(), name="me"),
]
