from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerial, SeatSerial, BookingSerial
from django.contrib.auth.decorators import login_required

class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerial
    queryset = Movie.objects.all()

class SeatViewSet(viewsets.ModelViewSet):
    serializer_class = SeatSerial
    queryset = Seat.objects.all()

class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerial
    queryset = Booking.objects.all()

def movie_view(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movie_list': movies})

def seat_view(request):
    seats = Seat.objects.all()
    return render(request, 'bookings/seat_booking.html', {'seat_list': seats})

@login_required
def booking_view(request):
    user = request.user
    bookings = Booking.objects.filter(user=user)
    return render(request, 'bookings/booking_history.html', {'booking_list': bookings})

@login_required
def booking_seat(request):
    if request.method == 'POST':
        seat_id = request.POST.get('seat_id')
        seat =  Seat.objects.get(id=seat_id)

        seat.is_booked = True
        seat.save()

        movie = Movie.objects.first()

        booking = Booking.objects.create(user=request.user, seat=seat, movie=movie)
        
        return redirect('booking_history')
    return redirect('seat_booking')