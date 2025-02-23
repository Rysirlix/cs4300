from django.urls import path
from .views import movie_view, seat_view, booking_view, booking_seat

urlpatterns = [
    path('movies', movie_view, name='movie_list'),
    path('seats', seat_view, name='seat_booking'),
    path('bookings', booking_view, name='booking_history'),
    path('booking_seat', booking_seat, name='booking_seat'),
]