from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet

# Create a router and register the ViewSet
router = DefaultRouter()
router.register(r'', TransactionViewSet, basename='transaction')  # No redundant prefix

urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs
]