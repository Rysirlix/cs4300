from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField()

    def __str__(self):
        return self.title +' | '+ self.description[:30] + '... | ' + str(self.release_date)

class Seat(models.Model):
    seat_number = models.CharField(max_length=25, unique=True)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return self.seat_number + ' | ' + ('Booked' if self.is_booked else 'Available')


class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField (auto_now_add=True)

    def __str__(self):
        return  self.user.username +' | '+ self.movie.title +' | '+ self.seat.seat_number