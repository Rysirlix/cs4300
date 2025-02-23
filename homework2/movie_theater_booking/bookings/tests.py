from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from .models import Movie, Seat, Booking
from django.contrib.auth.models import User

class ApiTestBase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_user(username='Test', password='test')
        self.movie = Movie.objects.create(
            title='Test',
            description='Test description',
            release_date='2012-12-12',
            duration=120
        )
        self.seat = Seat.objects.create(seat_number='T1', is_booked=False)
        self.client.login(username='Test', password='test') 

    def test_get_movies(self):

        response = self.client.get('/api/movies/')
        self.assertEqual(len(response.data),1)
        self.assertEqual(response.data[0]['title'], self.movie.title)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_book_seat(self):

        response = self.client.put(f'/api/seats/{self.seat.id }/', {'is_booked': True})
        self.seat.refresh_from_db()
        self.assertTrue(self.seat.is_booked)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_seats(self):

        response = self.client.get('/api/seats/')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['seat_number'], self.seat.seat_number)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_bookings(self):

        Booking.objects.create(user=self.user,movie=self.movie, seat=self.seat)
        response = self.client.get('/api/bookings/')
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['movie'], self.movie.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)