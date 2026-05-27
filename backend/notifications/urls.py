from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import NotificationViewSet

# Create a router and register the NotificationViewSet
# This automatically generates the following URL patterns:
# GET     /api/notifications/     - list all notifications for the current user
# GET     /api/notifications/{id}/       - retrieve a single notification
# PATCH   /api/notifications/{id}/mark_read/
router = DefaultRouter()
router.register("", NotificationViewSet, basename="notifications")

urlpatterns = [path("", include(router.urls))]
