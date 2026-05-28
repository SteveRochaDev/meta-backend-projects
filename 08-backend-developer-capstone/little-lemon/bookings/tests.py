from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.utils import timezone
from .models import Booking

class BookingTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.booking = Booking.objects.create(
            name="Test Customer",
            no_of_guests=2,
            booking_date=timezone.now()
        )

    def test_get_bookings(self):
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)