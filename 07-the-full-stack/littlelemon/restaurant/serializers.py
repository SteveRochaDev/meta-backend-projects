from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, data):

        reservation_date = data['reservation_date']
        reservation_slot = data['reservation_slot']

        if Booking.objects.filter(
            reservation_date=reservation_date,
            reservation_slot=reservation_slot
        ).exists():

            raise serializers.ValidationError(
                "This time slot is already booked."
            )

        return data