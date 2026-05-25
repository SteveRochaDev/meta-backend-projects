from django.shortcuts import render
from rest_framework import generics

from .models import Booking
from .serializers import BookingSerializer


def book(request):
    return render(request, 'book.html')


class BookingViewSet(generics.ListCreateAPIView):

    serializer_class = BookingSerializer

    def get_queryset(self):

        queryset = Booking.objects.all()

        date = self.request.query_params.get('date')

        if date:
            queryset = queryset.filter(reservation_date=date)

        return queryset