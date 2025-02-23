from rest_framework import serializers
from .models import Movie, Seat, Booking

class MovieSerial(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class SeatSerial(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'
        extra_kwargs = {'seat_number': {'required': False}}

class BookingSerial(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'