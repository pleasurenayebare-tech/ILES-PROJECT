from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import NotificationViewSet

# Create a router and register the NotificationViewSet
router = DefaultRouter()
router.register("", NotificationViewSet, basename="notifications")

urlpatterns = [path("", include(router.urls))]
