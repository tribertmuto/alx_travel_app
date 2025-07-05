"""
URL configuration for listings app.
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets
router = DefaultRouter()
# router.register(r'listings', views.ListingViewSet)
# router.register(r'bookings', views.BookingViewSet)

app_name = 'listings'

urlpatterns = [
    # API endpoints
    path('', include(router.urls)),
    
    # Custom endpoints
    path('health/', views.health_check, name='health_check'),
    
    # Add your custom URL patterns here
    # path('listings/', views.ListingListView.as_view(), name='listing_list'),
    # path('listings/<int:pk>/', views.ListingDetailView.as_view(), name='listing_detail'),
]