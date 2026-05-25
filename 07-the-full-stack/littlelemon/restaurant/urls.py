from django.urls import path
from .views import book, BookingViewSet

urlpatterns = [
    path('book/', book, name='book'),
    path('bookings/', BookingViewSet.as_view()),
]